# Generated by Django 4.1.1 on 2022-10-06 11:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_remove_company_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='user_login',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
