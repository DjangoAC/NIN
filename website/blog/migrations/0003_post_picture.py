# Generated by Django 2.1.2 on 2018-11-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
