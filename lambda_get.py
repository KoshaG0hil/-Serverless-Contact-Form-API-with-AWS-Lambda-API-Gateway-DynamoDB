import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ContactSubmissions')

def lambda_handler(event, context):
    try:
        response = table.scan()
        data = response['Items']

        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
