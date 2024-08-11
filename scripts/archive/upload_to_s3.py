import json
import boto3
from io import BytesIO

# Initialize AWS clients
s3 = boto3.client('s3')
sqs = boto3.client('sqs')

# Configuration
local_file_path = '/Users/harishnaidugaddam/Downloads/Real_Time_Data_Processing/scripts/ecommerce_100_transactions.json'
s3_bucket_name = 'ecommercetransactions'
s3_file_key = 'ecommerce_100_transactions.json'  # Adjusted file key for clarity
queue_url = 'https://sqs.us-east-2.amazonaws.com/637423377183/realtimedataprocessing-transactions-queue'

def upload_file_to_s3(local_file_path, bucket_name, s3_file_key):
    """
    Upload a file to S3.

    :param local_file_path: The path to the local file to upload.
    :param bucket_name: The name of the S3 bucket.
    :param s3_file_key: The key (path) where the file will be saved in S3.
    """
    s3.upload_file(local_file_path, bucket_name, s3_file_key)
    print(f"Uploaded {local_file_path} to S3 bucket {bucket_name} as {s3_file_key}")

def read_json_from_s3(bucket_name, file_key):
    """
    Read a JSON file directly from S3 without downloading it.

    :param bucket_name: The name of the S3 bucket.
    :param file_key: The key (path) of the file in S3.
    :return: Parsed JSON data.
    """
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read().decode('utf-8')
    data = json.loads(file_content)
    return data

def send_message_to_sqs(queue_url, message_body):
    """
    Send a message to the specified SQS queue.

    :param queue_url: The URL of the SQS queue.
    :param message_body: The body of the message to send.
    """
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message_body
    )
    print("Message Sent: ", response)

def process_and_send_messages(json_data, queue_url):
    """
    Process JSON data and send each item to SQS.

    :param json_data: Parsed JSON data.
    :param queue_url: The URL of the SQS queue.
    """
    for item in json_data:
        message_body = json.dumps(item)
        send_message_to_sqs(queue_url, message_body)

if __name__ == "__main__":
    # Upload JSON file to S3
    upload_file_to_s3(local_file_path, s3_bucket_name, s3_file_key)

    # Read JSON file from S3
    data = read_json_from_s3(s3_bucket_name, s3_file_key)

    # Process JSON data and send messages to SQS
    process_and_send_messages(data, queue_url)
