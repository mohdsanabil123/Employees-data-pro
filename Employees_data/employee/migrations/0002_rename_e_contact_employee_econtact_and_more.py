# Generated by Django 4.1.7 on 2023-03-28 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='e_contact',
            new_name='econtact',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='e_email',
            new_name='eemail',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='e_id',
            new_name='eid',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='e_name',
            new_name='ename',
        ),
    ]
