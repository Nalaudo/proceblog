# Generated by Django 4.1 on 2022-09-25 03:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user',
            field=models.CharField(max_length=250),
        ),
    ]
