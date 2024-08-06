import boto3

lambda_client = boto3.client('lambda')

def delete_lambda_function(function_name):
    response = lambda_client.delete_function(FunctionName=function_name)
    print(f"Lambda function deleted: {response}")

delete_lambda_function('ProcessRealtimeDataTransactions')
