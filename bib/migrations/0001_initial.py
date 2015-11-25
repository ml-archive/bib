# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('request_type', models.CharField(max_length=255, null=True, blank=True)),
                ('request_path', models.CharField(max_length=255, null=True, blank=True)),
                ('sent_at', models.CharField(max_length=255, null=True, blank=True)),
                ('request_body', models.TextField(null=True, blank=True)),
                ('request_origin', models.CharField(max_length=255, null=True, blank=True)),
                ('response_data', models.TextField(null=True, blank=True)),
                ('response_code', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
    ]
