# Generated by Django 5.0.3 on 2024-05-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipmessageservice', '0014_alter_firm_firm_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='api_url',
            field=models.URLField(blank=True, db_comment='api地址', null=True, verbose_name='api地址'),
        ),
    ]
