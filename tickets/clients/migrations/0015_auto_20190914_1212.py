# Generated by Django 2.1.5 on 2019-09-14 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_auto_20190914_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='email1',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email0',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email2',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email3',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email4',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email5',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email6',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email7',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email8',
        ),
        migrations.RemoveField(
            model_name='client',
            name='email9',
        ),
    ]
