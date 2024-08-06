import boto3

sqs = boto3.client('sqs')

def delete_sqs_queue(queue_url):
    response = sqs.delete_queue(QueueUrl=queue_url)
    print(f"SQS queue deleted: {response}")

delete_sqs_queue('https://sqs.us-east-2.amazonaws.com/637423377183/realtimedataprocessing-transactions-queue')
