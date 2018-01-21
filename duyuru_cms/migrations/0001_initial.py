# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('duyuru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CokDuyuruPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='duyuru_cms_cokduyurupluginmodel', parent_link=True, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TekDuyuruPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='duyuru_cms_tekduyurupluginmodel', parent_link=True, to='cms.CMSPlugin')),
                ('duyuru', models.ForeignKey(to='duyuru.Duyuru')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
