# Generated by Django 3.1.4 on 2020-12-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0002_delete_playername'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
    ]
