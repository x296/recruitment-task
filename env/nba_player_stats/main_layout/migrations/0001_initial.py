# Generated by Django 3.1.4 on 2021-01-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=4)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('position', models.CharField(max_length=32)),
                ('height_feet', models.CharField(max_length=32)),
                ('height_inches', models.CharField(max_length=32)),
                ('weight_pounds', models.CharField(max_length=32)),
                ('team_name', models.CharField(max_length=32)),
                ('conference', models.CharField(max_length=32)),
                ('division', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Statistics',
            },
        ),
    ]