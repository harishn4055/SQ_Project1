import boto3

def create_sns_topic(topic_name):
    """
    Create an SNS topic with the specified name.

    :param topic_name: The name of the SNS topic.
    :return: The ARN of the created SNS topic.
    """
    # Initialize the SNS client
    sns = boto3.client('sns')

    # Create the SNS topic
    response = sns.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    
    print("SNS Topic Created: ", response)
    return topic_arn

if __name__ == "__main__":
    topic_name = 'realtimedataprocessing-transactions-topic'
    topic_arn = create_sns_topic(topic_name)
    print(f"SNS Topic ARN: {topic_arn}")
