# Generated by Django 3.1.2 on 2020-10-28 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phantomname', '0002_ghostname'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhantomName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ghostname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phantomname.ghostname')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
