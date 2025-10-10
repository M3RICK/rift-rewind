import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def get_dynamodb_reasources():
    region = os.getenv('AWS_DEFAULT_REGION')
    
    if not region:
        raise ValueError(
            "AWS_DEFAULT_REGION not found in environment variables! "
            "Make sure .env file exists and contains the correct reigon"
        )
    return boto3.resource('dynamodb', region_name=region)