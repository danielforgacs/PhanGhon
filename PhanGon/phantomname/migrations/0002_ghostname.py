# Generated by Django 3.1.2 on 2020-10-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phantomname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GhostName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
