import os

import dotenv

dotenv.load_dotenv()

topic_arn = os.getenv("SNS_TOPIC_ARN")
queue_arn = os.getenv("SQS_QUEUE_ARN")
queue_url = os.getenv("SQS_QUEUE_URL")
