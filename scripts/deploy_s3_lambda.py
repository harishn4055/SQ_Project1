import boto3
import zipfile
import os
from botocore.exceptions import ClientError

# AWS configuration
LAMBDA_FUNCTION_NAME = 'upload_to_s3_lambda'
LAMBDA_ROLE_ARN = 'arn:aws:iam::637423377183:role/LambdaExecutionRole'
ZIP_FILE_NAME = 'upload_to_s3_lambda.zip'
LAMBDA_FILE_NAME = 'upload_to_s3_lambda.py'

def zip_lambda_code():
    """
    Zip the Lambda function code.
    """
    if not os.path.isfile(LAMBDA_FILE_NAME):
        raise FileNotFoundError(f"{LAMBDA_FILE_NAME} not found. Please check the file path.")

    with zipfile.ZipFile(ZIP_FILE_NAME, 'w') as zipf:
        zipf.write(LAMBDA_FILE_NAME, arcname=LAMBDA_FILE_NAME)
    print(f"Zipped {LAMBDA_FILE_NAME} into {ZIP_FILE_NAME}")

def deploy_lambda_function():
    """
    Deploy or update the Lambda function.
    """
    client = boto3.client('lambda')

    with open(ZIP_FILE_NAME, 'rb') as f:
        zipped_code = f.read()

    try:
        # Check if the function exists
        response = client.get_function(FunctionName=LAMBDA_FUNCTION_NAME)
        function_exists = True
        print(f"Lambda function '{LAMBDA_FUNCTION_NAME}' already exists. Updating function.")
        response = client.update_function_code(
            FunctionName=LAMBDA_FUNCTION_NAME,
            ZipFile=zipped_code
        )
        print("Lambda function code updated.")
    except client.exceptions.ResourceNotFoundException:
        function_exists = False
        print(f"Lambda function '{LAMBDA_FUNCTION_NAME}' does not exist. Creating function.")
        response = client.create_function(
            FunctionName=LAMBDA_FUNCTION_NAME,
            Runtime='python3.8',
            Role=LAMBDA_ROLE_ARN,
            Handler='upload_to_s3_lambda.lambda_handler',
            Code=dict(ZipFile=zipped_code),
            Timeout=300,  # 5 minutes
            MemorySize=128
        )
        print("Lambda function created.")

    print("Lambda function deployed/updated:")
    print(response)

def clean_up():
    """
    Clean up local files.
    """
    if os.path.exists(ZIP_FILE_NAME):
        os.remove(ZIP_FILE_NAME)
        print(f"Deleted local zip file: {ZIP_FILE_NAME}")

if __name__ == "__main__":
    try:
        zip_lambda_code()
        deploy_lambda_function()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        clean_up()
