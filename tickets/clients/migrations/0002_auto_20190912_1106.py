# Generated by Django 2.1.5 on 2019-09-12 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
