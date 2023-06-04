"""
DineSeater allows only specific users to sign up.
This lambda function is to filter user email at Cognito signing up process.
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
        # TODO : check if the email is associated with any Dineseater supported restaurants.
        # TODO : add restaurant attribute to user (ex. restaurant : gilson). Use aws-sdk.
    except Exception:
        raise Exception("The email does not associate with restaurants. Please contact DineSeater.")
    
    
    # Return to Amazon Cognito
    return event