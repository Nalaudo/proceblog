# Generated by Django 4.1 on 2022-09-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Borrador'), (1, 'Publico')], default=0),
        ),
    ]