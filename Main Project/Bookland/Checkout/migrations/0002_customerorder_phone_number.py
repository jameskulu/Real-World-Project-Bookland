# Generated by Django 3.0.8 on 2020-08-05 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
