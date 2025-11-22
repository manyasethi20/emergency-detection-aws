# Real-Time Emergency Detection System using AWS Rekognition

This project detects emergencies such as fire, smoke, explosions, and accidents from images uploaded to Amazon S3.  
It uses AWS Rekognition for image analysis and AWS SNS for sending notifications.

## Features
• Automatic emergency detection  
• Serverless architecture  
• Email/SMS alerts using Amazon SNS  
• JSON output stored in S3  
• Works entirely on AWS cloud  

## Architecture Overview
1. User uploads an image to S3.
2. S3 triggers AWS Lambda.
3. Lambda sends the image to Rekognition.
4. Rekognition returns labels with confidence.
5. Lambda checks for emergency keywords.
6. Output JSON is saved to S3.
7. SNS sends alert if emergency is detected.

## AWS Services Used
• Amazon S3  
• AWS Lambda  
• Amazon Rekognition  
• Amazon SNS  
• IAM Roles  
• CloudWatch Logs  

## How to Deploy
1. Create an S3 input and output bucket.
2. Create an SNS topic and subscription.
3. Create a Lambda function and upload the code.
4. Add environment variables:
   - OUTPUT_BUCKET  
   - SNS_TOPIC_ARN  
5. Add S3 trigger to Lambda.
6. Upload images to S3 to test.
   
## Folder Structure
emergency-detection-aws/
│
├── lambda/
│ └── lambda_function.py
│
├── samples/
│ └── sample-output.json
│
└── README.md


