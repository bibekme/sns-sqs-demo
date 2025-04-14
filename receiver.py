import json

import boto3

from variables import queue_url

sqs = boto3.client("sqs")

messages = sqs.receive_message(
    QueueUrl=queue_url, MaxNumberOfMessages=10, WaitTimeSeconds=0
)

print("Message received from SQS:")
print(json.dumps(messages, indent=2))
