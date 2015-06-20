# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('keywords_string', models.CharField(max_length=500, blank=True, editable=False)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(max_length=2000, help_text='Leave blank to have the URL auto-generated from the title.', blank=True, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(max_length=500, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', blank=True, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description', default=True)),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", blank=True, null=True, verbose_name='Published from', db_index=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", blank=True, null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('relevant_files', mezzanine.core.fields.FileField(max_length=1000, null=True, blank=True, verbose_name='Archive de la présentation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PresentationCategory',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, auto_created=True, parent_link=True, to='pages.Page', serialize=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('presentations', models.ManyToManyField(to='presentation.Presentation', blank=True, verbose_name='Présentations')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name_plural': 'Catégories de présentation',
                'verbose_name': 'Catégorie de présentation',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='presentation',
            name='categories',
            field=models.ManyToManyField(to='presentation.PresentationCategory', blank=True, verbose_name='Catégories'),
        ),
        migrations.AddField(
            model_name='presentation',
            name='site',
            field=models.ForeignKey(to='sites.Site', editable=False),
        ),
        migrations.AddField(
            model_name='presentation',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='presentations', verbose_name='Author'),
        ),
    ]
