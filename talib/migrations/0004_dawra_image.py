# Generated by Django 2.0.7 on 2018-08-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talib', '0003_auto_20180804_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='dawra',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
