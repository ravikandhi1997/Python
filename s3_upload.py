import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(file_name, bucket_name, object_name=None, region="ap-south-1"):
    if object_name is None:
        object_name = file_name

    # Create S3 client with the region explicitly set
    s3 = boto3.client('s3', region_name=region)

    try:
        # Upload file with public-read access
        s3.upload_file(
            file_name,
            bucket_name,
            object_name,
            ExtraArgs={'ACL': 'public-read', 'ContentType': 'text/html'}
        )

        print(f"✅ File '{file_name}' uploaded successfully to '{bucket_name}/{object_name}'.")
        print(f"🌐 View it at: http://{bucket_name}.s3-website.{region}.amazonaws.com/{object_name}")

    except FileNotFoundError:
        print("❌ File not found. Please check the path.")
    except NoCredentialsError:
        print("❌ AWS credentials not configured. Run 'aws configure' first.")
    except ClientError as e:
        print(f"❌ AWS Client Error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")

# ✅ Raw string path to avoid '\P' issue
upload_to_s3(r"D:\Python\sample.html", "my-ravi-789344", "sample.html")
