"""
DineSeater allows only specific users to sign up.
This lambda function is to enrich token with user's business into ID-TOKEN.
"""

import json
from email_allowlist import userEmail_to_business 

def lambda_handler(event, context):
    try:
        email = event['request']['userAttributes']['email']
        # emit log to Cloudwatch
        print ("User email = ", email)
        if email not in userEmail_to_business : 
            raise Exception("not associated email")
            
        add_business_name_to_user_attributes(event, userEmail_to_business[email])
        add_business_name_to_token_id(event, userEmail_to_business[email])
        
    except Exception:
        raise Exception("The email does not associate with restaurants. Please contact DineSeater.")
    
    
    # Return to Amazon Cognito
    return event
    
def add_business_name_to_user_attributes (event, business_name_value):
    try:
        add_user_attribute(event, 'business_name', business_name_value)
    except Exception:
        raise Exception("exception occurred during creating request for \
                         adding business_name to user attribute")

def add_user_attribute (event, attribute_key, attribute_value):
    user_attributes = event['request']['userAttributes']
    user_attributes[attribute_key] = attribute_value
    event['response']['userAttributes'] = user_attributes

def add_business_name_to_token_id (event, business_name_value):
    try:
        add_claim_to_token_id(event, 'business_name', business_name_value)
    except Exception:
        raise Exception("exception occurred during creating request for \
                         adding business_name to token_id")

def add_claim_to_token_id (event, claim_key, claim_value):
    event['response']['claimsOverrideDetails'] = {
        'claimsToAddOrOverride': {
            claim_key : claim_value
        }
    }   