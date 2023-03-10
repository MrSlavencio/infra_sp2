# Generated by Django 2.2.16 on 2022-11-09 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20221109_2253'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='review',
            name='unique_author_title',
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title'), name='unique_author_title'),
        ),
    ]
