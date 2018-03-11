import boto3, subprocess

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/083630338242/HackTJ'

response = sqs.receive_message(
    QueueUrl=queue_url,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)

message = response['Messages'][0]
body = response['Messages'][0]["Body"]
receipt_handle = message['ReceiptHandle']

# Delete received message from queue
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)
print('Received and deleted message: %s' % body)

identified_object = subprocess.call(['./tensorflow/classify.sh'])

'''
response = client.receive_message(QueueUrl=queue_url)
if response["Messages"][0]["Body"] is "true":
    identified_object = subprocess.call(['./tensorflow/classify.sh'])
    response = client.delete_message(
    QueueUrl='string',
    ReceiptHandle='string')
'''
