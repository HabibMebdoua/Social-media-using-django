# Generated by Django 4.1.5 on 2023-01-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_follower_profile_follower_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default='user.png', upload_to='profile_imgs'),
        ),
    ]