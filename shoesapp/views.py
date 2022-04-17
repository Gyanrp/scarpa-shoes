from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from random import randrange
from myapp.models import product as pro
from myapp.models import Category

# Create your views here.
def registration(request):
    if request.method == 'POST':
        try:
            Register.objects.get(email=request.POST['email'])
            return render(request,'registration.html',{'msg':'Your Email is already registered'})
        except:
            if request.POST['password']==request.POST['cpassword']:
                global temp
                temp={
                    'name' : request.POST['name'],
                    'mobile' : request.POST['mobile'],
                    'email' : request.POST['email'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Shoes App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'cotp.html',{'otp':otp})
            return render(request,'registration.html',{'msg':'Both Password Is not Match'})
    return render(request,'registration.html')

def cotp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            Register.objects.create(
                name = temp['name'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                password = temp['password']
            )
            msg = "Account is Created"
            return render(request,'login.html',{'msg':msg})
        return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'OTP Is Not Match'})
    # return redirect('registration')
    return render(request,'cotp.html')


def login(request):
    try:
        Register.objects.get(email=request.session['clientemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Register.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['clientemail'] = uid.email
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'registration.html',{'msg':'Email is not registered'})
        return render(request,'login.html')
def clogout(request):
    del request.session['clientemail']
    return redirect('index')

def forgotpass(request):
    if request.method == 'POST':
        try:
            uid=Register.objects.get(email=request.POST['email'])
            if uid.email == request.POST['email']:
                otp = randrange(1000,9999)
                message = f'Your OTP is {otp}. please enter correctly'
                subject = 'welcome to scarpa'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'re-password.html',{'otp' : otp,'Email':request.POST['email']})
        except:
            return render(request,'registration.html',{'msg':'email is not register'})
    return render(request,'forgotpass.html')

def repass(request):
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = Register.objects.get(email=request.POST['email'])
                if request.POST['password'] == request.POST['otp']:
                    uid.password = request.POST['otp']  
                    uid.save()
                    request.session['clientemail'] = uid.email
                    return redirect('index')
                return render(request,'re-password.html',{'msg' : 'incorrect password','uid': uid })
            except:
                return render(request,'re-password.html',{'msg' : 'Email is not register '})
        return render(request,'re-password.html')

def index(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'index.html',{'uid':uid,'pro':product})
    except:
        return render(request,'index.html',{'pro':product})
    
def allproducts(request):
    product = pro.objects.filter(active=True)
    if request.method == 'POST':
        product= list(pro.objects.filter(name__contains=request.POST['search'],active=True))
        product += list(pro.objects.filter(brand__contains=request.POST['search'],active=True))
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'allproducts.html',{'uid':uid,'pro':product})
    except:
        return render(request,'allproducts.html',{'pro':product})

def cpassword(request):
    uid = Register.objects.get(email=request.session['clientemail'])
    if request.method == 'POST':
        if uid.password == request.POST['opassword']:
            if request.POST['npassword'] == request.POST['cpassword']:
                uid.password = request.POST['npassword']
                uid.save()
                return redirect('index')
            return render(request,'cpassword.html',{'msg':'Both password are not same'})
        return render(request,'cpassword.html',{'msg':'old password is not correct'})
    return render(request,'cpassword.html')

def contact(request):

    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg,'uid':uid})
        return render(request,'contact.html',{'uid':uid})
    except:
        if request.method == 'POST':
            Contact.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message']
            )
            msg='Complant is Added'
            return render(request,'contact.html',{'msg':msg})
        return render(request,'contact.html')
def kid(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'kid.html',{'uid':uid,'pro':product})
    except:
        return render(request,'kid.html',{'pro':product})

def about(request):
    return render(request,'about.html')
def men(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'men.html',{'uid':uid,'pro':product})
    except:
        return render(request,'men.html',{'pro':product})

def women(request):
    product = pro.objects.filter(active=True)
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'women.html',{'uid':uid,'pro':product})
    except:
         return render(request,'women.html',{'pro':product})   

def checkout(request):
    return render(request,'checkout.html')

def order(request):
    return render(request,'order-complete.html')



def userprofile(request):
    uid = Register.objects.get(email=request.session['clientemail'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.email= request.POST['email']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        print(request.FILES)
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'userprofile.html',{'uid':uid,'msg':'Profile Updated'})
    return render(request,'userprofile.html',{'uid':uid})

def product_details(request,pk):
    product = pro.objects.get(id=pk)
    creview=Review.objects.all().count
    review=Review.objects.all()
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        return render(request,'product-detail.html',{'uid':uid,'pro':product,'creview':creview,'review':review})
    except:
        return render(request,'product-detail.html',{'pro':product,'creview':creview,'review':review})

def review(request,pk):
    product = pro.objects.get(id=pk)
    creview=Review.objects.all().count
    review=Review.objects.all()
    try:
        uid = Register.objects.get(email=request.session['clientemail'])
        if request.method=='POST':
            Review.objects.create(
                user=uid,
                product=product,
                name=request.POST['name'],
                message=request.POST['review']
            )
            ms='Review is Send'
            return render(request,'review.html',{'uid':uid,'pro':product,'ms':ms})
        return render(request,'review.html',{'uid':uid,'pro':product,'creview':creview,'review':review})
    except:
        return redirect('login')
def cart(request):
    return render(request,'cart.html')
def add(request):
    return render(request,'add-to-wishlist.html')
