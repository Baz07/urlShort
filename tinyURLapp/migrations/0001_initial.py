# Generated by Django 3.1.7 on 2021-02-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='short_url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=1000, verbose_name='URL')),
                ('short_url', models.CharField(max_length=20)),
            ],
        ),
    ]
