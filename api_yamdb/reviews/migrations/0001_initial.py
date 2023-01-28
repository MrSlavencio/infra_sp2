# Generated by Django 2.2.16 on 2022-11-09 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reviews.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название категории', max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(help_text='Адрес для страницы с группой', unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название жанра', max_length=200, verbose_name='Жанр')),
                ('slug', models.SlugField(help_text='Адрес для страницы с жанром', unique=True, verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название произведения', max_length=200, verbose_name='Произведение')),
                ('year', models.IntegerField()),
                ('description', models.TextField(blank=True, help_text='Описание произведения', max_length=255, null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, db_column='category', help_text='Категория, к которой относится произведение', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='reviews.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(help_text='Жанры произведения', related_name='titles', to='reviews.Genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.IntegerField(validators=[reviews.validators.validate_score])),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('title_id', models.ForeignKey(db_column='title_id', on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review_id', models.ForeignKey(db_column='review_id', on_delete=django.db.models.deletion.CASCADE, to='reviews.Review')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
        migrations.AddConstraint(
            model_name='review',
            constraint=models.UniqueConstraint(fields=('author', 'title_id'), name='unique_author_title'),
        ),
    ]
