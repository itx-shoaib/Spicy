# Generated by Django 4.0.3 on 2022-05-02 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='view',
        ),
    ]
