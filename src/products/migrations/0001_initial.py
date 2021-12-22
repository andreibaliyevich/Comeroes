# Generated by Django 3.2.8 on 2021-11-07 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import products.utilities


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('slug', models.SlugField(max_length=64, unique=True, verbose_name='Slug')),
                ('logo', models.ImageField(help_text='Recommend: 300 x 160 px.', upload_to=products.utilities.get_manufacturer_logo_path, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('main_image', models.ImageField(help_text='Recommend: 764 x 905 px.', upload_to=products.utilities.get_product_image_path, verbose_name='Main image')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Price')),
                ('old_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Old price')),
                ('rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='Rating')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.manufacturer', verbose_name='Manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='AccessoryProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('category', models.CharField(blank=True, choices=[('', 'Select category'), ('1', 'Bags & Backpacks'), ('2', 'Jewelry'), ('3', 'Tech Accessories'), ('4', 'Travel Accessories'), ('5', 'Hats'), ('6', 'Scarves'), ('7', 'Socks')], default='', max_length=1, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Accessory',
                'verbose_name_plural': 'Accessories',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ClothesProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('category', models.CharField(blank=True, choices=[('', 'Select category'), ('1', 'T-Shirts'), ('2', 'Jackets & Sweatshirts'), ('3', 'Robes & Sleepwear'), ('4', 'Kids & Baby'), ('5', 'Tank Tops')], default='', max_length=1, verbose_name='Category')),
                ('size', models.CharField(blank=True, choices=[('', 'Select size'), ('XS', 'X-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large'), ('XXL', 'XX-Large'), ('XXXL', 'XXX-Large')], default='', max_length=4, verbose_name='Size')),
                ('color', models.CharField(blank=True, choices=[('', 'Select color'), ('ff0000', 'Red'), ('00ff00', 'Green'), ('0000ff', 'Blue'), ('000000', 'Black'), ('ffffff', 'White'), ('808080', 'Gray'), ('ffc0cb', 'Pink'), ('800080', 'Purple')], default='', max_length=6, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Clothes',
                'verbose_name_plural': 'Clothes',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ComicBookProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('category', models.CharField(blank=True, choices=[('', 'Select category'), ('1', 'Marvel'), ('2', 'DC'), ('3', 'Star Wars')], default='', max_length=1, verbose_name='Category')),
                ('publication_format', models.CharField(blank=True, max_length=16, verbose_name='Publication format')),
                ('number_pages', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of pages')),
                ('published', models.DateField(blank=True, null=True, verbose_name='Published')),
                ('binding', models.CharField(blank=True, choices=[('', 'Select binding'), ('1', 'Paperback'), ('2', 'Hardcover')], default='', max_length=1, verbose_name='Binding')),
                ('language', models.CharField(choices=[('en', 'English'), ('ru', 'Русский'), ('be', 'Беларуская')], default='en', max_length=2, verbose_name='Language')),
            ],
            options={
                'verbose_name': 'Comic Book',
                'verbose_name_plural': 'Comics',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='HomeDecorProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('category', models.CharField(blank=True, choices=[('', 'Select category'), ('1', 'Mugs'), ('2', 'Ornaments & Holiday Decor'), ('3', 'Posters & Prints'), ('4', 'Stationery')], default='', max_length=1, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Home Decor',
                'verbose_name_plural': 'Home Decor',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ToyProduct',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('category', models.CharField(blank=True, choices=[('', 'Select category'), ('1', 'Marvel'), ('2', 'DC'), ('3', 'Star Wars')], default='', max_length=1, verbose_name='Category')),
                ('country', models.CharField(blank=True, choices=[('', 'Select country'), ('US', 'USA'), ('CN', 'China'), ('RU', 'Russia')], default='', max_length=2, verbose_name='Manufacturer country')),
                ('material', models.CharField(blank=True, choices=[('', 'Select material'), ('1', 'Plastic'), ('2', 'Plastic / electronics'), ('3', 'Plastic / LED'), ('4', 'Polyester'), ('5', 'Plush')], default='', max_length=1, verbose_name='Material')),
                ('packing_size', models.CharField(blank=True, help_text='millimetres', max_length=32, verbose_name='Packing size')),
                ('weight', models.PositiveSmallIntegerField(blank=True, help_text='gram', null=True, verbose_name='Weight')),
            ],
            options={
                'verbose_name': 'Toy',
                'verbose_name_plural': 'Toys',
                'ordering': ['-created_at', '-updated_at', '-id'],
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Recommend: 764 x 905 px.', upload_to=products.utilities.get_product_image_path, verbose_name='Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
                'ordering': ['product', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(verbose_name='Count')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
                'ordering': ['product', 'store'],
                'unique_together': {('product', 'store')},
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(None, 'Choose rating'), (5, '5 stars'), (4, '4 stars'), (3, '3 stars'), (2, '2 stars'), (1, '1 star')], verbose_name='Rating')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('dislikes', models.ManyToManyField(blank=True, related_name='review_dislikes', to=settings.AUTH_USER_MODEL, verbose_name='Dislikes')),
                ('likes', models.ManyToManyField(blank=True, related_name='review_likes', to=settings.AUTH_USER_MODEL, verbose_name='Likes')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['-created_at', '-id'],
                'unique_together': {('product', 'user')},
            },
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('be', 'Беларуская')], max_length=2, verbose_name='Language')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Product Translation',
                'verbose_name_plural': 'Product Translations',
                'ordering': ['product', 'language'],
                'unique_together': {('product', 'language')},
            },
        ),
    ]