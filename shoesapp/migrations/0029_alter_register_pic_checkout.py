# Generated by Django 4.0.2 on 2022-04-24 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_product_qty'),
        ('shoesapp', '0028_alter_register_pic_delete_checkout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo9.png', upload_to='Profile Pic'),
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=60)),
                ('qty', models.IntegerField()),
                ('size', models.CharField(max_length=60)),
                ('pay_mode', models.CharField(choices=[('cod', 'cod'), ('online', 'online')], max_length=50)),
                ('pay_id', models.CharField(blank=True, max_length=30, null=True)),
                ('verify', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=0)),
                ('pay_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.register')),
            ],
        ),
    ]
