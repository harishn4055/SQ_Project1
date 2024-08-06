import boto3

cloudwatch = boto3.client('cloudwatch')

def delete_cloudwatch_alarm(alarm_name):
    response = cloudwatch.delete_alarms(AlarmNames=[alarm_name])
    print(f"CloudWatch alarm deleted: {response}")

delete_cloudwatch_alarm('ProcessRealtimeDataTransactions-Error-Alarm')
delete_cloudwatch_alarm('ProcessRealtimeDataTransactions-Duration-Alarm')
delete_cloudwatch_alarm('realtimedataprocessing-transactions-table-Throttle-Alarm')
