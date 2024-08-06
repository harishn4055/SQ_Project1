# Real-Time Data Processing Project

## Overview

This repository contains a real-time data processing pipeline using AWS services. The pipeline processes e-commerce transactions and stores them in DynamoDB while monitoring and alerting using CloudWatch.

## Components

- **AWS Lambda**: Processes SQS messages and interacts with DynamoDB and SNS.
- **DynamoDB**: Stores transaction data.
- **SNS**: Sends notifications for large transactions.
- **SQS**: Queues transaction messages.
- **CloudWatch**: Monitors Lambda and DynamoDB with alarms.

## Setup

1. **Configure AWS CLI**: Ensure AWS CLI is configured with the appropriate credentials and region.
2. **Run Scripts**:
   - `create_sns_topic.py`: Creates SNS topic and subscribes.
   - `create_cloudwatch_alarm.py`: Sets up CloudWatch alarms.
   - `trigger_cloudwatch_alarms.py`: Triggers alarms for testing.
   - `trigger_dynamodb_throttle.py`: Simulates DynamoDB throttling.
   - `delete_resources.py`: Deletes all created resources.

## Testing

- **Lambda Errors**: Triggered with `trigger_lambda_error()`.
- **Lambda Duration**: Triggered with `trigger_lambda_duration()`.
- **DynamoDB Throttling**: Simulated with `trigger_dynamodb_throttle()`.

## Cleanup

To stop all services and clean up resources:

- **Stop/Remove Lambda Functions**: Use AWS Console or `delete_lambda_function()` script.
- **Delete DynamoDB Tables**: Use AWS Console or `delete_dynamodb_table()` script.
- **Delete SNS Topics**: Use AWS Console or `delete_sns_topic()` script.
- **Delete SQS Queues**: Use AWS Console or `delete_sqs_queue()` script.
- **Delete CloudWatch Alarms**: Use AWS Console or `delete_cloudwatch_alarm()` script.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

