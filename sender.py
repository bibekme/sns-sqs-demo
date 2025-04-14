import boto3

from variables import topic_arn, queue_arn

sns = boto3.client("sns")

sns.subscribe(TopicArn=topic_arn, Protocol="sqs", Endpoint=queue_arn)

message = sns.publish(
    TopicArn=topic_arn, Message="Hello, this is a test message from SNS!"
)

print("Message published to SNS topic with ID:", message.get("MessageId"))
