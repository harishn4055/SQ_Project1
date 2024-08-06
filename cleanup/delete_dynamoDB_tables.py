import boto3

dynamodb = boto3.client('dynamodb')

def delete_dynamodb_table(table_name):
    response = dynamodb.delete_table(TableName=table_name)
    print(f"DynamoDB table deleted: {response}")

delete_dynamodb_table('realtimedataprocessing-transactions-table')
