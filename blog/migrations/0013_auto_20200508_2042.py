# Generated by Django 3.0.5 on 2020-05-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200508_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_img',
            field=models.ImageField(default='blog_covers/img5.jpg', upload_to='blog_covers/'),
        ),
    ]
