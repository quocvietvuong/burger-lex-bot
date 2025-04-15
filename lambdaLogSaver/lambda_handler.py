import json
import boto3
import base64
import gzip

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'orderburgerbot-cloudwatch-log-saver-bucket'

    # Get the log data from the event
    log_data = event['awslogs']['data']

    # Decode and decompress the log data
    decoded_data = base64.b64decode(log_data)

    uncompressed_payload = gzip.decompress(decoded_data).decode('utf-8')

    # Load the log data as JSON
    log_events = json.loads(uncompressed_payload)

    # Process each log event
    for log_event in log_events['logEvents']:
        # Create a unique filename for the log entry
        file_name = f"logs/{log_event['id']}.json"

        # Upload log data to S3
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(log_event))

    return {
        'statusCode': 200,
        'body': json.dumps('Logs saved to S3!')
    }