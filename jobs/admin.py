from django.contrib import admin
from .models import Jobs
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class JobsResource(resources.ModelResource):

    def get_export_headers(self):
        headers = super().get_export_headers()
        for i, h in enumerate(headers):
            if h == 'company_logo':
                headers[i] = "job.company_logo"
            if h == 'company_logo':
                headers[i] = "job.company_logo"
            if h == 'job_title':
                headers[i] = "job.job_title"
            if h == 'company_name':
                headers[i] = "job.company_name"
            if h == 'company_email':
                headers[i] = "job.company_email"
            if h == 'is_approved':
                headers[i] = "job.is_approved"
            if h == 'is_active':
                headers[i] = "job.is_active"
            if h == 'is_filled':
                headers[i] = "job.is_filled"
            if h == 'is_featured':
                headers[i] = "job.is_featured"
            if h == 'company_url':
                headers[i] = "job.company_url"
            if h == 'job_country':
                headers[i] = "job.job_country"

            if h == 'job_state':
                headers[i] = "job.job_state"
            if h == 'job_zip_code':
                headers[i] = "job.job_zip_code"
            if h == 'job_city':
                headers[i] = "job.job_city"
            if h == 'job_address':

                headers[i] = "job.job_address"
            if h == 'category':
                headers[i] = "job.category"
            if h == 'type':
                headers[i] = "job.type"
            if h == 'payment_method':
                headers[i] = "job.payment_method"
            if h == 'job_created_at':
                headers[i] = "job.job_created_at"
            if h == 'job_expires_at':
                headers[i] = "job.job_expires_at"
            if h == 'company_website':
                headers[i] = "job.company_website"
            if h == 'job_description':
                headers[i] = "job.job_description"
            if h == 'wpjobboard_am_data':
                headers[i] = "job.wpjobboard_am_data"
            if h == 'company_country':
                headers[i] = "job.company_country"
            if h == 'company_state':
                headers[i] = "job.company_state"
            if h == 'company_zip_code':
                headers[i] = "job.company_zip_code"
            if h == 'company_location':
                headers[i] = "job.company_location"
            if h == 'company_size':
                headers[i] = "job.company_size"
            if h == 'remote_ready':
                headers[i] = "job.remote_ready"
            if h == 'twitter_link':
                headers[i] = "job.twitter_link"
            if h == 'linkedin_link':
                headers[i] = "job.linkedin_link"
            if h == 'facebook_link':
                headers[i] = "job.facebook_link"

            if h == 'company_info':
                headers[i] = "job.company_info"

            if h == 'is_public':
                headers[i] = "job.is_public"

            if h == 'company_slogan':
                headers[i] = "job.company_slogan"

        return headers

    class Meta:
        model = Jobs


class BookAdmin(ImportExportModelAdmin):
    resource_class = JobsResource


admin.site.register(Jobs, BookAdmin)
