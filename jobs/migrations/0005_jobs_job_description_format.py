# Generated by Django 4.1.1 on 2022-10-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_jobs_company_country_jobs_company_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='job_description_format',
            field=models.CharField(default='html', max_length=50),
        ),
    ]
