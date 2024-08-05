import boto3

def receive_message_from_sqs(queue_url):
    """
    Receive a message from the specified SQS queue.

    :param queue_url: The URL of the SQS queue.
    """
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    # Receive a message from the SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=5
    )
    
    print("Message Received: ", response)

if __name__ == "__main__":
    queue_url = 'https://sqs.us-east-1.amazonaws.com/637423377183/realtimedataprocessing-transactions-queue'
    receive_message_from_sqs(queue_url)
