# Generated by Django 4.1 on 2023-03-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician', '0002_alter_musician_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='age',
            field=models.IntegerField(),
        ),
    ]