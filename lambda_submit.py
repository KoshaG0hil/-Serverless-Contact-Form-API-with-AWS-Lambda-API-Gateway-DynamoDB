import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactSubmissions')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        table.put_item(
            Item={
                'email': email,
                'name': name,
                'message': message
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Hi {name}, your message has been saved!'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
