# Generated by Django 3.1 on 2020-10-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='dineeAdmin', max_length=200),
        ),
    ]
