# Generated by Django 2.2.2 on 2019-06-26 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(upload_to='pet'),
        ),
    ]
