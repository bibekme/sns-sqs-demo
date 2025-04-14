import os

import boto3
from botocore.exceptions import ClientError

from variables import topic_arn, queue_url

sns = boto3.client("sns")
sqs = boto3.client("sqs")

try:
    sns.delete_topic(TopicArn=topic_arn)
    print("Deleted SNS topic:", topic_arn)
except ClientError as e:
    print(f"Error deleting SNS topic: {e.response['Error']['Message']}")

try:
    sqs.delete_queue(QueueUrl=queue_url)
    print("Deleted SQS queue:", queue_url)
except ClientError as e:
    if e.response["Error"]["Code"] == "AWS.SimpleQueueService.NonExistentQueue":
        print("SQS queue already deleted or never existed.")
    else:
        print(f"Error deleting SQS queue: {e.response['Error']['Message']}")

if os.path.exists(".env"):
    os.remove(".env")
    print("Deleted .env file")
else:
    print(".env file not found")
