from rest_framework import serializers
from api.models import Campaign

# Serializers define the API representation.

class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'url', 'category_id', 'category', 'currencycode', 'current_amount', 'goal', 'donators', 'days_active', 'title', 'description',
         'has_beneficiary', 'turn_off_donations', 'user_id', 'user_first_name', 'user_last_name', 'user_profile_url', 'deactivated',
          'campaign_image_url', 'launch_date', 'campaign_hearts', 'social_share_total', 'social_share_last_update', 'location_city',
           'location_country', 'location_zip', 'charity_valid', 'charity_npo_id', 'charity_name', 'is_fulfilled_numeric', 'percent_fulfilled', 'success', 'ranking']
