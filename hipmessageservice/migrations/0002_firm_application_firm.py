# Generated by Django 5.0 on 2024-02-29 05:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipmessageservice', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gmt_created', models.DateTimeField(auto_now_add=True, db_comment='创建时间', verbose_name='创建时间')),
                ('is_deleted', models.BooleanField(db_comment='删除标记', default=False, verbose_name='删除标记')),
                ('gmt_updated', models.DateTimeField(auto_now=True, db_comment='最后更新时间', verbose_name='最后更新时间')),
                ('firm_id', models.UUIDField(db_comment='唯一标识', default=uuid.uuid4, verbose_name='厂商唯一标识')),
                ('firm_name', models.CharField(db_comment='厂商名称', max_length=64, verbose_name='厂商名称')),
                ('firm_name_en', models.CharField(blank=True, db_comment='厂商英文名称', max_length=64, null=True, verbose_name='厂商英文名称')),
                ('creator', models.ForeignKey(db_comment='创建人', default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related_creator', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
                ('updater', models.ForeignKey(db_comment='修改者', default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_related_updater', related_query_name='%(app_label)s_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='修改者')),
            ],
            options={
                'verbose_name': '厂商信息',
                'verbose_name_plural': '厂商信息',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='firm',
            field=models.ForeignKey(blank=True, db_comment='厂商名称', null=True, on_delete=django.db.models.deletion.PROTECT, to='hipmessageservice.firm', verbose_name='厂商名称'),
        ),
    ]