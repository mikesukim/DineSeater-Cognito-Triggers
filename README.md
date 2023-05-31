# DineSeater Cognito Triggers

## Background
DineSeater leverages AWS Cognito as their Authentication/Authorization server.

Within the Cognito's Authentication/Authorization workflow, the injection of personal proprietary code becomes necessary for the following reasons:

1. filter user_email for when signing up. Only associated email can sign up to DineSeater.

2. ID Token enrichment.

Injection can be achieved via Cognito Trigger.
