import unittest
from unittest.mock import MagicMock, patch
import os
import boto3

class TestLambdaFunction(unittest.TestCase):

    @patch('boto3.client')
    def test_lambda_handler(self, mock_boto3_client):
        # Mock S3 client and object
        s3_mock = MagicMock()
        s3_mock.get_object.return_value = {
            'Body': MagicMock(read=MagicMock(return_value=b'fake_image_data'))
        }
        s3_mock.put_object.return_value = {}

        # Inject the mocked S3 client
        mock_boto3_client.return_value = s3_mock

        # Import the Lambda function after patching
        from src.image_opti_flow.lambda_scripts.image_processor import lambda_handler

        # Define a sample event
        event = {
            'key': 'sample_image.jpg'
        }

        # Set environment variables
        os.environ['SOURCE_BUCKET'] = 'source-bucket'
        os.environ['DESTINATION_BUCKET'] = 'destination-bucket'

        # Call the Lambda function
        result = lambda_handler(event, None)

        # Assertions
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['body'], 'Image processed and uploaded successfully.')
        s3_mock.get_object.assert_called_once_with(Bucket='source-bucket', Key='sample_image.jpg')
        s3_mock.put_object.assert_called_once_with(
            Bucket='destination-bucket',
            Key='processed/sample_image.jpg',
            Body=b'fake_image_data'
        )

if __name__ == '__main__':
    unittest.main()
