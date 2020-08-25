# Generated by Django 3.0.7 on 2020-08-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author_name',
            field=models.CharField(max_length=50, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(verbose_name='publication_date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(verbose_name='review_text'),
        ),
    ]