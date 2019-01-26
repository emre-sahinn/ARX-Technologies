# Generated by Django 2.1.5 on 2019-01-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='features',
            new_name='feature',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='votes',
        ),
        migrations.AddField(
            model_name='choice',
            name='feature_price',
            field=models.IntegerField(default=-1),
        ),
    ]