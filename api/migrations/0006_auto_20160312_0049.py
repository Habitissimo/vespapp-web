# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_signthing_faq_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightingfaq',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='faq_images/'),
        ),
    ]