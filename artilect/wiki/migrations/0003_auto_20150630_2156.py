# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_wikiarticle_comments_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikiarticle',
            name='histoire',
            field=mezzanine.core.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikiarticle',
            name='lundi_files',
            field=models.FileField(verbose_name='Archive de la présentation', max_length=1000, blank=True, null=True, upload_to='presentations'),
        ),
        migrations.AddField(
            model_name='wikiarticle',
            name='lundi_soir',
            field=mezzanine.core.fields.RichTextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='wikiarticle',
            name='resume',
            field=mezzanine.core.fields.RichTextField(null=True, blank=True),
        ),
    ]
