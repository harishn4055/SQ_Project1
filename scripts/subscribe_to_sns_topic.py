import boto3

def subscribe_to_sns_topic(topic_arn, protocol, endpoint):
    """
    Subscribe to an SNS topic.

    :param topic_arn: The ARN of the SNS topic.
    :param protocol: The protocol to use (e.g., 'email').
    :param endpoint: The endpoint to receive notifications (e.g., email address).
    :return: The subscription ARN.
    """
    # Initialize the SNS client
    sns = boto3.client('sns')

    # Subscribe to the SNS topic
    response = sns.subscribe(
        TopicArn=topic_arn,
        Protocol=protocol,
        Endpoint=endpoint
    )
    
    print("SNS Subscription: ", response)
    return response['SubscriptionArn']

if __name__ == "__main__":
    topic_arn = 'arn:aws:sns:us-east-2:637423377183:realtimedataprocessing-transactions-topic'
    protocol = 'email'  # Use 'email' for email subscriptions
    endpoint = 'reddyalu05@gmail.com'  # Replace with your email address
    subscription_arn = subscribe_to_sns_topic(topic_arn, protocol, endpoint)
    print(f"SNS Subscription ARN: {subscription_arn}")
