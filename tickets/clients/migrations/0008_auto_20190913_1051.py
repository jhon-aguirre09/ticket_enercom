# Generated by Django 2.1.5 on 2019-09-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20190913_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
