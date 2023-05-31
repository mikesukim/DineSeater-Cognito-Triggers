import unittest
from lambda_function import (
    add_business_name_to_user_attributes,
    add_business_name_to_token_id,
    get_user_attributes,
    set_user_attributes,
    get_claims_override_details,
    set_claims_override_details
)

class TestLambdaFunction(unittest.TestCase):
    def setUp(self):
        # Set up the event object for testing
        self.event = {
            "version": "1",
            "triggerSource": "TokenGeneration_HostedAuth",
            "region": "us-east-1",
            "userPoolId": "us-east-1_U7DgGJukj",
            "userName": "b539ee54-e8a1-4de9-9fe3-101aff57d3cf",
            "callerContext": {
                "awsSdkVersion": "aws-sdk-unknown-unknown",
                "clientId": "71m3jlg6nokn4ha61aslj93cpi"
            },
            "request": {
                "userAttributes": {
                    "sub": "b539ee54-e8a1-4de9-9fe3-101aff57d3cf",
                    "cognito:email_alias": "mikesungunkim@gmail.com",
                    "cognito:user_status": "CONFIRMED",
                    "email_verified": "true",
                    "given_name": "Michael",
                    "family_name": "Kim",
                    "email": "mikesungunkim@gmail.com"
                },
                "groupConfiguration": {
                    "groupsToOverride": [],
                    "iamRolesToOverride": [],
                    "preferredRole": None
                }
            },
            "response": {
                "claimsOverrideDetails": None
            }
        }

    def test_add_business_name_to_user_attributes(self):
        business_name_value = "12345678"

        add_business_name_to_user_attributes(self.event, business_name_value)

        user_attributes = get_user_attributes(self.event)
        self.assertIn('business_name', user_attributes)
        self.assertEqual(user_attributes['business_name'], business_name_value)

    def test_add_business_name_to_token_id(self):
        business_name_value = "12345678"

        add_business_name_to_token_id(self.event, business_name_value)

        claims_override_details = get_claims_override_details(self.event)
        self.assertIn('claimsToAddOrOverride', claims_override_details)
        self.assertEqual(claims_override_details['claimsToAddOrOverride'], {'business_name': business_name_value})

    def test_get_user_attributes(self):
        user_attributes = get_user_attributes(self.event)
        self.assertIsInstance(user_attributes, dict)
        self.assertEqual(user_attributes, self.event['request']['userAttributes'])

    def test_set_user_attributes(self):
        user_attributes = {'business_name': '12345678'}

        set_user_attributes(self.event, user_attributes)

        self.assertEqual(self.event['response']['userAttributes'], user_attributes)

    def test_get_claims_override_details(self):
        claims_override_details = get_claims_override_details(self.event)
        self.assertIsInstance(claims_override_details, dict)
        self.assertEqual(claims_override_details, {})

    def test_set_claims_override_details(self):
        claims_override_details = {'claimsToAddOrOverride': {'business_name': '12345678'}}

        set_claims_override_details(self.event, claims_override_details)

        self.assertEqual(self.event['response']['claimsOverrideDetails'], claims_override_details)

if __name__ == '__main__':
    unittest.main()
