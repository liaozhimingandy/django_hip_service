# Generated by Django 5.0 on 2024-03-01 07:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipmessageservice', '0004_application_is_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_name',
            field=models.CharField(db_comment='系统名称', max_length=32, unique=True, verbose_name='系统名称'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='firm_id',
            field=models.UUIDField(db_comment='唯一标识', default=uuid.uuid4, unique=True, verbose_name='厂商唯一标识'),
        ),
        migrations.AlterField(
            model_name='firm',
            name='firm_name',
            field=models.CharField(db_comment='厂商名称', max_length=64, unique=True, verbose_name='厂商名称'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_lookup',
            field=models.BooleanField(blank=True, db_comment='是否为查询类接口', db_default=models.Value(False), default=False, null=True, verbose_name='是否为查询类接口'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_code',
            field=models.CharField(db_comment='服务代码', max_length=32, unique=True, verbose_name='服务代码'),
        ),
    ]