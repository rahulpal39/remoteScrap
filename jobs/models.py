
from datetime import timedelta
from email.policy import default
from enum import auto
from django.utils import timezone
from django.db import models

# Create your models here.

def in_three_days():
    return timezone.now() + timedelta(days=28)



class company(models.Model):
    company_logo=models.CharField(max_length=50,blank=True,null=True)
    company_name=models.CharField(max_length=50,blank=True,null=True)
    company_country=models.CharField(max_length=50,blank=True,null=True)
    company_state=models.CharField(max_length=50,blank=True,null=True)
    company_zip_code=models.CharField(max_length=50,blank=True,null=True)
    company_location=models.CharField(max_length=50,blank=True,null=True)
    user_email=models.CharField(max_length=50,blank=True,null=True)
    user_login=models.CharField(max_length=50,blank=True,null=True)
    company_website=models.CharField(max_length=50,blank=True,null=True)
    company_info=models.CharField(max_length=50,blank=True,null=True)
    is_public=models.CharField(max_length=50,blank=True,null=True)
    company_slogan=models.CharField(max_length=50,blank=True,null=True)
    group_image=models.CharField(max_length=50,blank=True,null=True)
    remote_ready=models.CharField(max_length=50,blank=True,null=True)
    company_size=models.CharField(max_length=50,blank=True,null=True)
    twitter_link=models.CharField(max_length=50,blank=True,null=True)
    linkedin_link=models.CharField(max_length=50,blank=True,null=True)
    facebook_link=models.CharField(max_length=50,blank=True,null=True)
    field_8=models.CharField(max_length=50,blank=True,null=True)
    field_5=models.CharField(max_length=50,blank=True,null=True)
    field_6=models.CharField(max_length=50,blank=True,null=True)
    field_7=models.CharField(max_length=50,blank=True,null=True)


class Jobs(models.Model):
    company=models.ForeignKey(company, verbose_name=("company"), on_delete=models.DO_NOTHING,blank=True,null=True)

    company_logo=models.ImageField()	
    job_title=models.CharField(max_length=50,blank=True,null=True)	
    company_name=models.CharField(max_length=50,blank=True,null=True)	
    company_email=models.EmailField()	
    is_approved=models.BooleanField(default=True)	
    is_active=models.BooleanField(default=True)	
    is_filled=models.BooleanField(default=False)	
    is_featured=models.BooleanField(default=False)	
    company_url=models.URLField()
    job_country=models.CharField(max_length=50,blank=True,null=True)	
    job_state=models.CharField(max_length=50,blank=True,null=True)	
    job_zip_code=models.CharField(max_length=50,blank=True,null=True)	
    job_city=models.CharField(max_length=50,blank=True,null=True)	
    job_address=models.CharField(max_length=50,blank=True,null=True)	
    category=models.CharField(max_length=50,blank=True,null=True)	
    type=models.CharField(max_length=50,blank=True,null=True)	
    payment_method=models.CharField(max_length=50,blank=True,null=True)	
    job_created_at=models.DateField(default=timezone.now)	
    job_expires_at=models.DateField(default=in_three_days)
    company_website=models.URLField()	
    job_description=models.TextField(unique=True) 	
    wpjobboard_am_data=models.URLField()	    
    company_country=models.CharField(max_length=50,blank=True,null=True)
    company_state=models.CharField(max_length=50,blank=True,null=True)
    company_zip_code=models.CharField(max_length=50,blank=True,null=True)
    company_location=models.CharField(max_length=50,blank=True,null=True)    
    company_info=models.CharField(max_length=50,blank=True,null=True)
    is_public=models.CharField(max_length=50,blank=True,null=True)
    company_slogan=models.CharField(max_length=50,blank=True,null=True)
    remote_ready=models.CharField(max_length=50,blank=True,null=True)
    company_size=models.CharField(max_length=50,blank=True,null=True)
    twitter_link=models.URLField()
    linkedin_link=models.URLField()
    facebook_link=models.URLField()	
    job_description_format=models.CharField(max_length=50,default='html')

    def __str__(self):
        return self.job_title


