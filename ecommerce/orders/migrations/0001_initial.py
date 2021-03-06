# Generated by Django 2.0.1 on 2018-01-24 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_cart_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=20)),
                ('status', models.CharField(choices=[('Cancelled', 'Cancelled'), ('Dispatched', 'Dispatched'), ('Shipped', 'Shipped'), ('Created', 'Created')], default='Created', max_length=40)),
                ('shipping_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
            ],
        ),
    ]
