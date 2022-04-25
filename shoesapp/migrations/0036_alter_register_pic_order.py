# Generated by Django 4.0.2 on 2022-04-24 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoesapp', '0035_alter_register_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='pic',
            field=models.ImageField(default='logo12.png', upload_to='Profile Pic'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=60)),
                ('pay_mode', models.CharField(choices=[('cod', 'cod'), ('online', 'online')], max_length=50)),
                ('pay_id', models.CharField(blank=True, max_length=30, null=True)),
                ('verify', models.BooleanField(default=False)),
                ('amount', models.IntegerField(default=0)),
                ('pay_at', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoesapp.cart')),
            ],
        ),
    ]