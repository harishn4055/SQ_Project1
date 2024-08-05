import boto3

def create_dynamodb_table(table_name):
    """
    Create a DynamoDB table with the specified name and schema.

    :param table_name: The name of the DynamoDB table.
    :return: The ARN of the created DynamoDB table.
    """
    # Initialize the DynamoDB client
    dynamodb = boto3.client('dynamodb')

    # Create the DynamoDB table
    response = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'transaction_id',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'transaction_id',
                'AttributeType': 'S'  # String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    
    print("DynamoDB Table Created: ", response)
    return response['TableDescription']['TableArn']

if __name__ == "__main__":
    table_name = 'realtimedataprocessing-transactions-table'
    table_arn = create_dynamodb_table(table_name)
    print(f"DynamoDB Table ARN: {table_arn}")
