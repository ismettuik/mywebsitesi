# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duyuru',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('kod', models.IntegerField()),
                ('baslik', models.CharField(max_length=200)),
                ('icerik', models.TextField()),
                ('eklenme_tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayinlansinmi', models.CharField(max_length=1, default='H', choices=[('E', 'Evet'), ('H', 'Hayır')])),
            ],
        ),
    ]
