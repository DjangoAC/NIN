# Generated by Django 2.1.2 on 2018-11-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
