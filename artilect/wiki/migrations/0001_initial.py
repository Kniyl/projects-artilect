# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, primary_key=True, parent_link=True, to='pages.Page', serialize=False)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name_plural': 'Wikis',
                'ordering': ('_order',),
                'verbose_name': 'Wiki',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='WikiArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, max_length=2000, null=True, verbose_name='URL', help_text='Leave blank to have the URL auto-generated from the title.')),
                ('_meta_title', models.CharField(blank=True, max_length=500, null=True, verbose_name='Title', help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description', default=True)),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')], default=2)),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Published from', help_text="With Published chosen, won't be shown until this time")),
                ('expiry_date', models.DateTimeField(blank=True, null=True, verbose_name='Expires on', help_text="With Published chosen, won't be shown after this time")),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(verbose_name='Show in sitemap', default=True)),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('site', models.ForeignKey(to='sites.Site', editable=False)),
                ('user', models.ForeignKey(related_name='wikiarticles', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('wikis', models.ManyToManyField(blank=True, to='wiki.Wiki', verbose_name='Wikis')),
            ],
            options={
                'verbose_name_plural': 'Articles de Wiki',
                'verbose_name': 'Article de Wiki',
            },
        ),
        migrations.AddField(
            model_name='wiki',
            name='articles',
            field=models.ManyToManyField(blank=True, to='wiki.WikiArticle', verbose_name='Articles'),
        ),
    ]
