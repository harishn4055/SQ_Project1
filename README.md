# Real-Time Data Processing Pipeline for E-Commerce Transactions

This project implements a real-time data processing pipeline for e-commerce transactions using AWS services like SQS, SNS, Lambda, DynamoDB, and CloudWatch. The pipeline ingests transaction data, processes and validates it, stores valid transactions in DynamoDB, and sends notifications for certain transaction events.

## Project Overview

### Objectives:
1. **Data Ingestion**: Queue incoming transaction data using SQS.
2. **Notification**: Send notifications using SNS for specific transaction events (e.g., large orders).
3. **Processing**: Use Lambda to process the transactions, validate the data, and store it in DynamoDB.
4. **Monitoring**: Monitor Lambda execution and DynamoDB performance using CloudWatch.

### Technologies Used:
- **Python**
- **AWS SQS (Simple Queue Service)**
- **AWS SNS (Simple Notification Service)**
- **AWS Lambda**
- **AWS DynamoDB**
- **AWS CloudWatch**
- **AWS IAM (Identity and Access Management)**
- **AWS SDK for Python (Boto3)**
- **AWS CLI**

## Repository Structure

| File Name                   | Description                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `setup_iam_role_and_policies.py`  | Script to create IAM roles and policies required for the pipeline.                                                                                  |
| `create_sqs_queue.py`       | Script to create an SQS queue to ingest e-commerce transactions.                                                                                    |
| `send_message_to_sqs.py`    | Script to send sample e-commerce transactions to the SQS queue.                                                                                     |
| `receive_message_from_sqs.py` | Script to receive messages from the SQS queue for processing.                                                                                     |
| `delete_message_from_sqs.py`  | Script to delete processed messages from the SQS queue.                                                                                            |
| `create_sns_topic.py`       | Script to create an SNS topic for sending notifications about specific transaction events.                                                          |
| `deploy_lambda.py`          | Script to deploy the main Lambda function for processing transactions from SQS and storing them in DynamoDB.                                         |
| `lambda_function.py`        | The core logic of the Lambda function that validates and processes the transaction data and stores it in DynamoDB.                                    |
| `invoke_lambda.py`          | Script to invoke the `upload_to_s3_lambda` function, which uploads local data to S3 and sends it to SQS.                                             |
| `create_dynamodb_table.py`  | Script to create a DynamoDB table where valid transactions are stored.                                                                               |
| `create_cloudwatch_alarm.py`| Script to create CloudWatch alarms to monitor Lambda execution and DynamoDB performance.                                                             |
| `trigger_cloudwatch_alarms.py`| Script to simulate scenarios that would trigger CloudWatch alarms.                                                                                |
| `ecommerce_100_transactions.json` | A JSON file containing sample e-commerce transactions used for testing the pipeline.                                                           |
| `upload_to_s3_lambda.py`    | Lambda function script for uploading data to S3 and triggering subsequent processing steps.                                                         |
| `deploy_s3_lambda.py`       | Script to deploy the `upload_to_s3_lambda` Lambda function that handles S3 events.                                                                   |

### Cleanup Scripts
These scripts are used to clean up AWS resources after the pipeline has been tested or when no longer needed. They ensure that unnecessary AWS resources are not left running, which could incur costs.

| File Name                   | Description                                                                                                                                         |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `delete_lambda_functions.py`| Script to delete Lambda functions created for the pipeline.                                                                                         |
| `delete_dynamoDB_tables.py`  | Script to delete DynamoDB tables created for storing transaction data.                                                                             |
| `delete_sns_topics.py`       | Script to delete SNS topics used for notifications in the pipeline.                                                                                |
| `delete_sqs_queue.py`        | Script to delete SQS queues used for transaction data ingestion.                                                                                   |
| `delete_cloudwatch_alarms.py`| Script to delete CloudWatch alarms set up for monitoring the pipeline.                                                                             |
| `delete_iam_roles.py`        | Script to delete IAM roles and associated policies used in the pipeline.                                                                           |

## How It Works

1. **Data Ingestion and S3 Upload**: The `invoke_lambda.py` script invokes the `upload_to_s3_lambda` function, which uploads local data from `ecommerce_100_transactions.json` to an S3 bucket and sends the data to an SQS queue.
2. **Transaction Processing with Lambda**: A Lambda function processes messages from the SQS queue, validates the transactions, and stores them in DynamoDB.
3. **SNS Notifications**: SNS sends notifications for specific events, such as when a large order is detected.
4. **Monitoring with CloudWatch**: CloudWatch monitors the Lambda function and DynamoDB performance, with alarms set up to notify you of any issues.

## Conclusion

This project demonstrates a comprehensive real-time data processing pipeline using AWS services. The system automatically handles data ingestion, processing, notification, and monitoring, ensuring a scalable and efficient e-commerce transaction processing system. The cleanup scripts ensure that the AWS environment is left clean and free of unused resources.

## Repository Link

[GitHub Repository](https://github.com/harishnaidu0207/SQ_Project1) - Link to the GitHub repository where the code and documentation are hosted.
