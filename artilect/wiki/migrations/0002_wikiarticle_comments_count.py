# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikiarticle',
            name='comments_count',
            field=models.IntegerField(editable=False, default=0),
        ),
    ]
