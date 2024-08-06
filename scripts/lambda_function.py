import json
import boto3
import logging
import time

# Initialize AWS clients
sqs = boto3.client('sqs')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# DynamoDB table name
DYNAMODB_TABLE = 'realtimedataprocessing-transactions-table'
# SNS topic ARN
SNS_TOPIC_ARN = 'arn:aws:sns:us-east-2:637423377183:realtimedataprocessing-transactions-topic'

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function handler to process SQS messages, validate data, store in DynamoDB, and send notifications.
    """
    table = dynamodb.Table(DYNAMODB_TABLE)
    
    # Check for test inputs to trigger alarms
    if 'test' in event:
        if event['test'] == 'error':
            raise Exception("Intentional error to trigger CloudWatch alarm")
        elif event['test'] == 'duration':
            time.sleep(10)  # Sleep for 10 seconds to exceed the duration threshold
            return {'statusCode': 200, 'body': json.dumps('Duration test completed')}
    
    for record in event.get('Records', []):
        try:
            # Get the message body
            message_body = json.loads(record['body'])
            amount = message_body.get('amount', 0)
            
            # Example validation: Check if amount is greater than 0
            if amount > 0:
                # Store valid transaction in DynamoDB
                response = table.put_item(Item=message_body)
                logger.info(f"Stored item: {message_body}")
                
                # Send notification via SNS only if amount > 50000
                if amount > 50000:
                    sns.publish(
                        TopicArn=SNS_TOPIC_ARN,
                        Message=json.dumps({'default': f"Large order detected: {message_body}"}),
                        MessageStructure='json'
                    )
                    logger.info(f"Notification sent for item: {message_body}")
                else:
                    logger.info(f"No notification sent (amount <= 50000): {message_body}")
            else:
                logger.info(f"Transaction not stored (amount = 0): {message_body}")
        
        except Exception as e:
            logger.error(f"Error processing record {record}: {str(e)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Transactions processed')
    }
