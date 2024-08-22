import json 

def lambda_handler(event, context):
    return {
        #returns this when its true
        'statusCode': 200,
        'body': json.dumps('Hello from our CI/CD workflows vscode, Ceesay is back!')
    }

#add to test push actions.