# Generated by Django 2.2 on 2020-11-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klin_url', models.CharField(max_length=1000, unique=True)),
                ('long_url', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
