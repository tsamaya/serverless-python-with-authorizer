from __future__ import print_function
import json


def generatePolicy(principalId, effect, methodArn):
    authResponse = {}
    authResponse['principalId'] = principalId

    if effect and methodArn:
        policyDocument = {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Sid': 'FirstStatement',
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': methodArn
                }
            ]
        }

        authResponse['policyDocument'] = policyDocument

    return authResponse


def authorizerFunc(event, context):
    userId = 'your-user-id'
    whole_auth_token = event.get('authorizationToken')
    print('Client token: ' + whole_auth_token)
    print('methodArn', event['methodArn'])
    return generatePolicy(userId, 'allow', event['methodArn'])
