# Generated by Django 2.1.5 on 2019-01-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190125_1206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='feature',
        ),
        migrations.AddField(
            model_name='choice',
            name='feature1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='feature2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='choice',
            name='feature3',
            field=models.CharField(default='', max_length=200),
        ),
    ]
