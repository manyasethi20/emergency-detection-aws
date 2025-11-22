import json
import boto3
import os

rekog = boto3.client('rekognition')
s3 = boto3.client('s3')
sns = boto3.client('sns')

OUTPUT_BUCKET = os.environ.get('OUTPUT_BUCKET')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        # Process only image files
        if not key.lower().endswith(('.jpg', '.jpeg', '.png')):
            print("Skipping non-image file:", key)
            continue

        # Detect labels
        response = rekog.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=15,
            MinConfidence=70
        )

        labels = response['Labels']

        # Emergency keywords
        emergency_keywords = [
            'Fire', 'Smoke', 'Explosion', 'Weapon', 'Gun', 'Accident', 'Injury'
        ]

        # Check emergency
        emergency_detected = any(
            label['Name'] in emergency_keywords for label in labels
        )

        # Save JSON output
        output_key = key + ".labels.json"
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=json.dumps(labels, indent=2),
            ContentType='application/json'
        )

        # Notify user if emergency found
        if emergency_detected:
            message = f"Emergency detected in image: {key}"
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Message=message,
                Subject="Emergency Alert"
            )

    return {"status": "completed"}
