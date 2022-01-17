# Generated by Django 3.2.9 on 2022-01-17 18:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coupons', '0001_initial'),
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(max_length=150, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address')),
                ('phone', models.CharField(max_length=21, validators=[django.core.validators.RegexValidator(message='Wrong format!', regex='^(\\s*)?(\\+)?([- _():=+]?\\d[- _():=+]?){9,16}(\\s*)?$')], verbose_name='Phone')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('discount', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Discount')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total cost')),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Failed'), ('3', 'Processing'), ('4', 'Shipped'), ('5', 'Completed'), ('6', 'Delayed'), ('7', 'Canceled'), ('8', 'Refunded')], default='1', max_length=1, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='coupons.coupon', verbose_name='Coupon')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.store', verbose_name='Store')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Price')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total price')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Ordered product',
                'verbose_name_plural': 'Ordered products',
            },
        ),
    ]
