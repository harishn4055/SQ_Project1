import boto3

def delete_message_from_sqs(queue_url, receipt_handle):
    """
    Delete a message from the specified SQS queue.

    :param queue_url: The URL of the SQS queue.
    :param receipt_handle: The receipt handle of the message to delete.
    """
    # Initialize the SQS client
    sqs = boto3.client('sqs')

    # Delete the message from the SQS queue
    response = sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )
    
    print("Message Deleted: ", response)

if __name__ == "__main__":
    queue_url = 'https://sqs.us-east-1.amazonaws.com/637423377183/realtimedataprocessing-transactions-queue'
    receipt_handle = 'AQEBR7xWoeblr4fiMK4CG2LD0z5aO6dQbH7qpbZjTkIWuKthraeT0UpwgT447zhxW8Y5HlL9pCxN4hPT3Oy1Osv5ZCUzoVzdj2ERxqsGKALahpj5drloQQIkDf+D5SGWhvPwWpB75RwY96r0Y/7IlSL63PBu8p0nRoiirea/L9awFxQA+jnkrs4acUqqGSp2hFg7hpSyXtgD9GKIak5b9TlGa7a9Osp5xTA976Li9vWDaltNech3K2f8QQasoZ81ZYgWO0khr+DZufnKe60mYdoOpqmV8w/ui4hbStvf9eogZCdqQonl/UfzUDqzaJy0dU3YPrXCs6kRGlwhPE3MNZh5sQdtS+Bip6KjSICs4Ibxlrc6dv3LJpmnEmwsKbBFPzSsMxe1HxRW6nHxwFYfsMtwrbhHEO0bXISa3VG1DYN1l3I='
    delete_message_from_sqs(queue_url, receipt_handle)
