import boto3
import json

# Initialize AWS Lambda client
lambda_client = boto3.client('lambda')

# Configuration
lambda_function_name = 'upload_to_s3_lambda'  

def invoke_lambda_function(function_name, payload):
    """
    Invoke the specified Lambda function with the given payload.
    
    :param function_name: The name of the Lambda function.
    :param payload: The payload to pass to the Lambda function.
    :return: The response from the Lambda function invocation.
    """
    try:
        response = lambda_client.invoke(
            FunctionName=function_name,
            InvocationType='RequestResponse',  
            Payload=json.dumps(payload)
        )
        response_payload = json.loads(response['Payload'].read().decode('utf-8'))
        return response_payload
    except Exception as e:
        print(f"Failed to invoke Lambda function: {e}")
        raise

if __name__ == "__main__":
    # Read file content from local file
    local_file_path = 'ecommerce_100_transactions.json'
    
    try:
        with open(local_file_path, 'r') as file:
            file_content = file.read()
    except Exception as e:
        print(f"Failed to read local file: {e}")
        raise

    # Create payload with file content
    payload = {
        "file_content": file_content
    }
    
    # Invoke the Lambda function
    response = invoke_lambda_function(lambda_function_name, payload)
    print("Lambda function response:")
    print(response)
