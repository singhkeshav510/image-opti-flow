import os
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = os.environ['SOURCE_BUCKET']
    destination_bucket = os.environ['DESTINATION_BUCKET']
    source_key = event['key']  # The key of the image in the source bucket

    # Fetch the image data from the source S3 bucket
    response = s3.get_object(Bucket=source_bucket, Key=source_key)
    image_data = response['Body'].read()

    # Your image processing code can go here.
    # You can modify the image_data as needed.

    # Upload the modified image to the destination S3 bucket
    destination_key = 'processed/' + source_key  # Modify the destination key as needed
    s3.put_object(Bucket=destination_bucket, Key=destination_key, Body=image_data)

    return {
        'statusCode': 200,
        'body': 'Image processed and uploaded successfully.'
    }
