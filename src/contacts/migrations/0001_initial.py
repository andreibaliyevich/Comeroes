# Generated by Django 3.2.9 on 2022-02-13 11:58

import contacts.utilities
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=21, validators=[django.core.validators.RegexValidator(message='Wrong format!', regex='^(\\s*)?(\\+)?([- _():=+]?\\d[- _():=+]?){9,16}(\\s*)?$')], verbose_name='Phone')),
                ('subject', models.CharField(blank=True, max_length=150, verbose_name='Subject')),
                ('content', models.TextField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ['-created_at', '-id'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('brest', 'Brest'), ('minsk', 'Minsk'), ('grodno', 'Grodno'), ('gomel', 'Gomel'), ('mogilev', 'Mogilev'), ('vitebsk', 'Vitebsk')], max_length=64, verbose_name='City')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326, verbose_name='Location')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, verbose_name='Keywords')),
                ('main_image', models.ImageField(help_text='Recommend: 1000 x 667 px.', upload_to=contacts.utilities.get_store_image_path, verbose_name='Main image')),
                ('customers_phone', models.CharField(max_length=21, verbose_name='Phone for customers')),
                ('support_phone', models.CharField(max_length=21, verbose_name='Phone for support')),
                ('customers_email', models.EmailField(max_length=254, verbose_name='Email for customers')),
                ('support_email', models.EmailField(max_length=254, verbose_name='Email for support')),
                ('time_weekdays_start', models.TimeField(verbose_name='Start time in weekdays')),
                ('time_weekdays_end', models.TimeField(verbose_name='End time in weekdays')),
                ('time_weekend_start', models.TimeField(verbose_name='Start time in weekend')),
                ('time_weekend_end', models.TimeField(verbose_name='End time in weekend')),
                ('is_main', models.BooleanField(default=False, verbose_name='Main')),
            ],
            options={
                'verbose_name': 'Store',
                'verbose_name_plural': 'Stores',
                'ordering': ['id'],
                'unique_together': {('city', 'address')},
            },
        ),
        migrations.CreateModel(
            name='StoreImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Recommend: 1000 x 667 px.', upload_to=contacts.utilities.get_store_image_path, verbose_name='Image')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Image of Store',
                'verbose_name_plural': 'Images of Store',
                'ordering': ['store', 'id'],
            },
        ),
        migrations.CreateModel(
            name='StoreTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('be', 'Беларуская')], max_length=2, verbose_name='Language')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Description')),
                ('meta_keywords', models.CharField(blank=True, help_text='Separate keywords with commas.', max_length=255, verbose_name='Keywords')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='contacts.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'Store Translation',
                'verbose_name_plural': 'Store Translations',
                'ordering': ['store', 'language'],
                'unique_together': {('store', 'language')},
            },
        ),
    ]
