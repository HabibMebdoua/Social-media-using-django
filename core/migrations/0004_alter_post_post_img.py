# Generated by Django 4.1.5 on 2023-01-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_likes_post_likes_num_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(default='user.png', upload_to='posts'),
        ),
    ]
