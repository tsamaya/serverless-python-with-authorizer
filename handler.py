from __future__ import print_function
import json


def hello(event, context):
    print('event', event)
    userId = None
    if 'requestContext' in event and 'authorizer' in event['requestContext']:
        userId = event['requestContext']['authorizer']['principalId']
    body = {
        "userId": userId,
        "event": event
    }

    response = {
        "statusCode": 200,
        "headers": {
            # Required for CORS support to work
            'Access-Control-Allow-Origin': '*',
            # Required for cookies, authorization headers with HTTPS
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps(body)
    }

    return response
