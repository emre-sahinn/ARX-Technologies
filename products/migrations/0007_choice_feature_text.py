# Generated by Django 2.1.5 on 2019-01-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_choice_feature_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='feature_text',
            field=models.CharField(default='', max_length=250),
        ),
    ]