# Generated by Django 4.2.16 on 2024-11-25 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobrole',
            name='frequency',
            field=models.IntegerField(default=0),
        ),
    ]
