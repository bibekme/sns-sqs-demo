import boto3
import json

sns = boto3.client("sns")
sqs = boto3.client("sqs")

topic_name = "MyTopic"
topic_arn = sns.create_topic(Name=topic_name)["TopicArn"]
print("SNS Topic ARN:", topic_arn)

queue_name = "MyQueue"
queue_url = sqs.create_queue(QueueName=queue_name)["QueueUrl"]
print("SQS Queue URL:", queue_url)

queue_attrs = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=["QueueArn"])
queue_arn = queue_attrs["Attributes"]["QueueArn"]
print("SQS Queue ARN:", queue_arn)

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Allow-SNS-SendMessage",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "SQS:SendMessage",
            "Resource": queue_arn,
            "Condition": {"ArnEquals": {"aws:SourceArn": topic_arn}},
        }
    ],
}

sqs.set_queue_attributes(QueueUrl=queue_url, Attributes={"Policy": json.dumps(policy)})

sns.subscribe(TopicArn=topic_arn, Protocol="sqs", Endpoint=queue_arn)

env_content = f"""\
SNS_TOPIC_ARN="{topic_arn}"
SQS_QUEUE_URL="{queue_url}"
SQS_QUEUE_ARN="{queue_arn}"
"""

with open(".env", "w") as f:
    f.write(env_content)

print("Environment variables written to .env file.")
