# Generated by Django 3.0.4 on 2020-05-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200515_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='a.jpg', upload_to='profile_pics'),
        ),
    ]
