# Generated by Django 3.2.21 on 2023-09-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_delete_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='station_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
