# Generated by Django 3.1.4 on 2020-12-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20201213_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
