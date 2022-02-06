# Generated by Django 3.2.9 on 2022-02-06 21:51

import accounts.utilities
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email address')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Last name')),
                ('avatar', easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=accounts.utilities.get_user_avatar_path, verbose_name='Avatar')),
                ('phone', models.CharField(blank=True, max_length=21, validators=[django.core.validators.RegexValidator(message='Wrong format!', regex='^(\\s*)?(\\+)?([- _():=+]?\\d[- _():=+]?){9,16}(\\s*)?$')], verbose_name='Phone')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('is_subscription', models.BooleanField(default=True, verbose_name='Is subscription')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
                ('last_visit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last visit')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=64, verbose_name='Locality')),
                ('street_house', models.CharField(max_length=128, verbose_name='Street, House')),
                ('porch', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Porch')),
                ('level', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Level')),
                ('apt_office', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Apt / office')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Is Primary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
                'ordering': ['id'],
            },
        ),
    ]
