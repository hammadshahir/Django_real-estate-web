# Generated by Django 2.2.2 on 2019-08-02 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 2, 21, 58, 18, 895205)),
        ),
    ]
