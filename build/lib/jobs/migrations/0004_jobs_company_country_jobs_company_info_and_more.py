# Generated by Django 4.1.1 on 2022-10-04 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_is_active_alter_jobs_is_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='company_country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_info',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_size',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_slogan',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='company_zip_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='facebook_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='is_public',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='linkedin_link',
            field=models.URLField(default=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='remote_ready',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='twitter_link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='wpjobboard_am_data',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
