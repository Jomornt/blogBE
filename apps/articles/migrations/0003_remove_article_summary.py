# Generated by Django 2.2 on 2020-02-21 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlecategory_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
    ]
