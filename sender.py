import boto3

from variables import topic_arn

sns = boto3.client("sns")

message = sns.publish(
    TopicArn=topic_arn, Message="Hello, this is a test message from SNS!"
)

print("Message published to SNS topic with ID:", message.get("MessageId"))
