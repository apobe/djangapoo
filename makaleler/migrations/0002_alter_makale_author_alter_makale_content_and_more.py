# Generated by Django 4.2.1 on 2023-05-14 21:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makaleler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makale',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Makale'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='makale',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
        migrations.CreateModel(
            name='commentt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentauthor', models.CharField(max_length=20, verbose_name='yazan')),
                ('commentcontent', models.CharField(max_length=200, verbose_name='icerik')),
                ('commentdate', models.DateTimeField(auto_now_add=True, verbose_name='tarih')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='makaleler.makale', verbose_name='Makale')),
            ],
        ),
    ]