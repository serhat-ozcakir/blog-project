# Generated by Django 3.2.9 on 2021-11-04 12:29

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211103_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='django.png', upload_to=blog.models.user_directory_path),
        ),
    ]
