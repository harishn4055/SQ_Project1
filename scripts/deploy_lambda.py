import boto3
import zipfile
import os

# AWS configuration
LAMBDA_FUNCTION_NAME = 'ProcessRealtimeDataTransactions'
LAMBDA_ROLE_ARN = 'arn:aws:iam::637423377183:role/LambdaExecutionRole'  # Replace with your IAM role ARN

def zip_lambda_code():
    """
    Zip the Lambda function code.
    """
    with zipfile.ZipFile('lambda_function.zip', 'w') as zipf:
        zipf.write('lambda_function.py', arcname='lambda_function.py')
#This step is optional if you're directly deploying the code without S3 upload
# def upload_to_s3():
#     """
#     Upload the zipped Lambda function code to an S3 bucket.
#     """
#     s3 = boto3.client('s3')
#     with open('lambda_function.zip', 'rb') as data:
#         s3.upload_fileobj(data, 'lambda_function.zip')

def deploy_lambda_function():
    """
    Deploy or update the Lambda function.
    """
    client = boto3.client('lambda')
    
    with open('lambda_function.zip', 'rb') as f:
        zipped_code = f.read()
    
    try:
        # Check if the function exists
        response = client.get_function(FunctionName=LAMBDA_FUNCTION_NAME)
        function_exists = True
    except client.exceptions.ResourceNotFoundException:
        function_exists = False
    
    if function_exists:
        # Update existing Lambda function
        response = client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=zipped_code
        )
    else:
        # Create new Lambda function
        response = client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime='python3.9',
            Role=LAMBDA_ROLE_ARN,
            Handler='lambda_function.lambda_handler',
            Code=dict(ZipFile=zipped_code),
            Timeout=60,
            MemorySize=128
        )
    
    print("Lambda function deployed/updated:")
    print(response)

def clean_up():
    """
    Clean up local files.
    """
    os.remove('lambda_function.zip')

if __name__ == "__main__":
    zip_lambda_code()
    deploy_lambda_function()
    clean_up()
