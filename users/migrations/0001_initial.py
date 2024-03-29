# Generated by Django 4.1.5 on 2023-01-24 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=1000, null=True)),
                ('location', models.CharField(choices=[('ALG', 'Algeria'), ('OUT', 'Not From Algeria')], max_length=100)),
                ('profile_img', models.ImageField(upload_to='profile_imgs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
