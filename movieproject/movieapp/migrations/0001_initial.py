# Generated by Django 4.1.3 on 2022-11-14 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dscrptn', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
