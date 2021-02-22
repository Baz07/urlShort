# Generated by Django 3.1.7 on 2021-02-22 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='custom_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=1000, verbose_name='Enter a Long URL')),
                ('hash_value', models.TextField(unique=True, verbose_name='Short/Hash value')),
            ],
        ),
    ]