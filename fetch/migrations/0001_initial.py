# Generated by Django 2.0.3 on 2018-03-18 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longURL', models.TextField()),
                ('shortURL', models.CharField(max_length=8)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
