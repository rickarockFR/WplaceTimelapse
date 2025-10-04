import boto3
import botocore.client


S3_ENDPOINT_URL = "https://objects.hydn.us/"
S3_BUCKET_NAME = "wplace-archive"
S3_REGION = "phx1"

image_list = []
def fetch_all_snapshots(s3, bucket: str):# -> list[Snapshot]:
    paginator = s3.get_paginator("list_objects_v2")
    pages = paginator.paginate(Bucket=bucket, Prefix="full/")

    #snapshots: list[Snapshot] = []
    for page in pages:
        for obj in page.get("Contents", []):
            key = obj.get("Key", "")

            fullname = key
            key = key.replace('.png','')
            key = key.replace('full/','')
            key = key.split('-')
            
            image_list.append([key[1], f'https://objects.hydn.us/wplace-archive/{fullname}', key[2], key[3], key[0], int(key[4]), int(key[5])])

s3 = boto3.client(
    's3',   # type: ignore
    region_name=S3_REGION,
    endpoint_url=S3_ENDPOINT_URL,
    config=botocore.client.Config(signature_version=botocore.UNSIGNED)
)


fetch_all_snapshots(s3, S3_BUCKET_NAME)

