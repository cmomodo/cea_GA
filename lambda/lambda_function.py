import json 

def lambda_handler(event, context):
    return {
        #returns this when its true
        'statusCode': 200,
        'body': json.dumps('Ceesay is back!')
    }