# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='relevant_files',
            field=models.FileField(upload_to='presentations', blank=True, max_length=1000, null=True, verbose_name='Archive de la présentation'),
        ),
    ]
