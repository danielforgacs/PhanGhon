# Generated by Django 3.1.2 on 2020-10-29 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phantomname', '0003_phantomname'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='phantomname',
            constraint=models.UniqueConstraint(fields=('user', 'ghostname'), name='unique_phantomname'),
        ),
    ]
