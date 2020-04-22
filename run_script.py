#!/usr/bin/env python3
import json

# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'arcticapi.settings'
import django
django.setup()

# regular imports
from api.models import Campaign

# main script
def main():

    # COVID 19

    with open('campaigns.json') as json_file:
        data2 = json.load(json_file)
    campaigns = data2['campaigns']

    print()
    print()
    print('Campaigns:')
    print()
    for camp in campaigns:
        dbcamp = Campaign()
        dbcamp.id = camp['id']
        dbcamp.url = camp['url']
        dbcamp.category_id = camp['category_id']
        dbcamp.category = camp['category']
        dbcamp.currencycode = camp['currencycode']
        dbcamp.current_amount = camp['current_amount']
        dbcamp.goal = camp['goal']
        dbcamp.donators = camp['donators']
        dbcamp.days_active = camp['days_active']
        dbcamp.title = camp['title']
        dbcamp.description = camp['description']
        dbcamp.has_beneficiary = camp['has_beneficiary']
        dbcamp.turn_off_donations = camp['turn_off_donations']
        dbcamp.user_id = camp['user_id']
        dbcamp.user_first_name = camp['user_first_name']
        dbcamp.user_last_name = camp['user_last_name']
        dbcamp.user_profile_url = camp['user_profile_url']
        dbcamp.deactivated = camp['deactivated']
        dbcamp.campaign_image_url = camp['campaign_image_url']
        dbcamp.launch_date = camp['launch_date']
        dbcamp.campaign_hearts = camp['campaign_hearts']
        dbcamp.social_share_total = camp['social_share_total']
        dbcamp.social_share_last_update = camp['social_share_last_update']
        dbcamp.location_city = camp['location_city']
        dbcamp.location_country = camp['location_country']
        dbcamp.location_zip = camp['location_zip']
        dbcamp.charity_valid = camp['charity_valid']
        dbcamp.charity_npo_id = camp['charity_npo_id']
        dbcamp.charity_name = camp['charity_name']
        dbcamp.is_fulfilled_numeric = camp['is_fulfilled_numeric']
        dbcamp.percent_fulfilled = camp['percent_fulfilled']
        dbcamp.success = camp['success']
        dbcamp.ranking = camp['ranking']
        dbcamp.save()

    print('Complete')
    # bootstrap
if __name__ == '__main__':
    main()
