import boto3

sns = boto3.client('sns')

def delete_sns_topic(topic_arn):
    response = sns.delete_topic(TopicArn=topic_arn)
    print(f"SNS topic deleted: {response}")

delete_sns_topic('arn:aws:sns:us-east-2:637423377183:realtimedataprocessing-transactions-topic')
