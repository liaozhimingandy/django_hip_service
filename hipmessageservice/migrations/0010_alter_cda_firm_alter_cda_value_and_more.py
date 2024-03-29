# Generated by Django 5.0 on 2024-03-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hipmessageservice', '0009_cda_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cda',
            name='firm',
            field=models.ManyToManyField(related_name='系统', to='hipmessageservice.firm', verbose_name='系统'),
        ),
        migrations.AlterField(
            model_name='cda',
            name='value',
            field=models.CharField(db_comment='文档代码', max_length=5, unique=True, verbose_name='文档代码'),
        ),
        migrations.AlterField(
            model_name='service',
            name='applications',
            field=models.ManyToManyField(related_name='系统', through='hipmessageservice.StatusShip', to='hipmessageservice.application', verbose_name='系统'),
        ),
    ]
