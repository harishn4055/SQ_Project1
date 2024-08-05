import boto3

# Initialize the boto3 client for Lambda
lambda_client = boto3.client('lambda', region_name='us-east-2')

# Define the Lambda function name and SQS queue ARN
function_name = 'ProcessRealtimeDataTransactions'
event_source_arn = 'arn:aws:sqs:us-east-2:637423377183:realtimedataprocessing-transactions-queue'

# Create the event source mapping
response = lambda_client.create_event_source_mapping(
    EventSourceArn=event_source_arn,
    FunctionName=function_name,
    BatchSize=10,
    Enabled=True
)

# Print the response
print(response)
