# Generated by Django 2.2.3 on 2019-07-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20190707_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='Add some summary here.'),
        ),
    ]
