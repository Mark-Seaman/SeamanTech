# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(null=True)),
                ('parent', models.ForeignKey(to='thot.Thot', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
