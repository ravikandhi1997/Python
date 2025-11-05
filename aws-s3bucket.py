import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        if region is None:
            # Create S3 client without specifying region
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # Create S3 client with region
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        print(f"✅ Successfully created bucket: {bucket_name}")

    except ClientError as e:
        # Catch specific AWS errors (like bucket already exists, invalid name, permissions)
        print("❌ AWS returned an error:")
        print(e.response['Error']['Code'], "-", e.response['Error']['Message'])

    except Exception as e:
        # Catch any other Python-related error
        print(f"⚠️ Unexpected error: {e}")

# Example usage
create_bucket('my-ravi-789344', 'ap-south-1')
