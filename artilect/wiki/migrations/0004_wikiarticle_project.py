# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_auto_20150630_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikiarticle',
            name='project',
            field=mezzanine.core.fields.RichTextField(null=True, blank=True),
        ),
    ]
