# Generated by Django 2.2.1 on 2019-05-23 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_messageinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MessageInfo',
        ),
    ]
