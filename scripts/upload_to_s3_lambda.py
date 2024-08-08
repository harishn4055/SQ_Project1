import json
import boto3
from botocore.exceptions import ClientError

# Initialize AWS clients
s3 = boto3.client('s3')
sqs = boto3.client('sqs')

# Configuration
s3_bucket_name = 'ecommercetransactions'
s3_file_key = 'ecommerce_100_transactions.json'
queue_url = 'https://sqs.us-east-2.amazonaws.com/637423377183/realtimedataprocessing-transactions-queue'

def upload_file_to_s3(file_content, bucket_name, s3_file_key):
    """
    Upload a file to S3.
    """
    try:
        s3.put_object(Bucket=bucket_name, Key=s3_file_key, Body=file_content)
        print(f"Uploaded to S3 bucket {bucket_name} as {s3_file_key}")
    except ClientError as e:
        print(f"Failed to upload to S3: {e}")
        raise

def read_json_from_s3(bucket_name, file_key):
    """
    Read a JSON file directly from S3 without downloading it.
    """
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = obj['Body'].read().decode('utf-8')
        data = json.loads(file_content)
        return data
    except ClientError as e:
        print(f"Failed to read from S3: {e}")
        raise

def send_message_to_sqs(queue_url, message_body):
    """
    Send a message to the specified SQS queue.
    """
    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        print("Message Sent: ", response)
    except ClientError as e:
        print(f"Failed to send message to SQS: {e}")
        raise

def process_and_send_messages(json_data, queue_url):
    """
    Process JSON data and send each item to SQS.
    """
    for item in json_data:
        message_body = json.dumps(item)
        send_message_to_sqs(queue_url, message_body)

def lambda_handler(event, context):
    """
    Lambda function handler.
    """
    # Extract file content from event
    file_content = event.get('file_content')
    
    if not file_content:
        raise ValueError("No file content found in the event.")

    # Upload JSON file to S3
    upload_file_to_s3(file_content, s3_bucket_name, s3_file_key)

    # Read JSON file from S3
    data = read_json_from_s3(s3_bucket_name, s3_file_key)

    # Process JSON data and send messages to SQS
    process_and_send_messages(data, queue_url)

    return {
        'statusCode': 200,
        'body': json.dumps('File processed and messages sent to SQS successfully.')
    }
