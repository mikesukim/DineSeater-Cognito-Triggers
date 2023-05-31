'''
Entry point of lambda function's execution.
This lambda function will be executed at pre-token-generation phase as Cognito trigger.
'''

import json

def lambda_handler(event, context):
    business_name = "12345678"
    
    add_business_name_to_user_attributes(event, business_name)
    add_business_name_to_token_id(event, business_name)
    
    return event


def add_business_name_to_user_attributes(event, business_name_value):
    try:
        user_attributes = get_user_attributes(event)
        user_attributes['business_name'] = business_name_value
        set_user_attributes(event, user_attributes)
    except Exception as e:
        print("add_business_name_to_user_attributes exception with error message : " + str(e))
        raise Exception("An exception occurred during the creation of a request to add business_name to user attributes.")


def add_business_name_to_token_id(event, business_name_value):
    try:
        claims_override_details = get_claims_override_details(event)
        claims_override_details['claimsToAddOrOverride'] = {'business_name': business_name_value}
        set_claims_override_details(event, claims_override_details)
    except Exception as e:
        print("add_business_name_to_token_id exception with error message : " + str(e))
        raise Exception("An exception occurred during the creation of a request to add business_name to token_id.")


def get_user_attributes(event):
    return event['request']['userAttributes']


def set_user_attributes(event, user_attributes):
    event['response']['userAttributes'] = user_attributes


def get_claims_override_details(event):
    if 'claimsOverrideDetails' not in event['response'] or \
        event['response']['claimsOverrideDetails'] is None :
        event['response']['claimsOverrideDetails'] = {}
    return event['response']['claimsOverrideDetails']


def set_claims_override_details(event, claims_override_details):
    event['response']['claimsOverrideDetails'] = claims_override_details