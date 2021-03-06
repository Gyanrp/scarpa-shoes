# Generated by Django 4.0.2 on 2022-04-19 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_product_qty'),
        ('shoesapp', '0017_delete_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=60)),
                ('qty', models.IntegerField()),
                ('cart', models.ManyToManyField(related_name='Cart', to='myapp.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shoesapp.register')),
            ],
        ),
    ]
