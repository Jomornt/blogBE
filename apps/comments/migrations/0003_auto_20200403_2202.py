# Generated by Django 2.2 on 2020-04-03 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentreply',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_replys', to='comments.Comment'),
        ),
    ]
