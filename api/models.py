from __future__ import unicode_literals

from django.db import models
from api.fields import JSONField
from rest_framework import routers, serializers, viewsets
import json


# Create your models here.

class Campaign(models.Model):
    url = models.TextField()
    category_id = models.IntegerField()
    category = models.TextField()
    currencycode = models.TextField(null=True, blank=True)
    current_amount = models.DecimalField(max_digits=15, decimal_places=2)
    goal = models.IntegerField()
    donators = models.IntegerField()
    days_active = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    has_beneficiary = models.BooleanField()
    turn_off_donations = models.BooleanField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    user_first_name = models.TextField(null=True, blank=True)
    user_last_name = models.TextField(null=True, blank=True)
    user_profile_url = models.TextField(null=True, blank=True)
    deactivated = models.BooleanField(null=True, blank=True)
    campaign_image_url = models.TextField(null=True, blank=True)
    launch_date = models.TextField(null=True, blank=True)
    campaign_hearts = models.IntegerField()
    social_share_total = models.IntegerField()
    social_share_last_update = models.TextField(null=True, blank=True)
    location_city = models.TextField(null=True, blank=True)
    location_country = models.TextField(null=True, blank=True)
    location_zip = models.TextField(null=True, blank=True)
    charity_valid = models.BooleanField(null=True, blank=True)
    charity_npo_id = models.TextField(null=True, blank=True)
    charity_name = models.TextField(null=True, blank=True)
    is_fulfilled_numeric = models.BooleanField(null=True, blank=True)
    percent_fulfilled = models.TextField(null=True, blank=True)
    success = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    ranking = models.IntegerField()
