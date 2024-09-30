#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import boto3

s3 = boto3.client('s3', region_name="us-east-1")

# List the buckets
response = s3.list_buckets()

# Iterate through the response
for r in response['Buckets']:
    print(r['Name'])


bucket = 'ds2022-zzz2bx'
local_file = 'cat.png'

resp = s3.put_object(
    Body=local_file, 
    Bucket=bucket,
    Key=local_file,
    ACL='public-read'
)

print(resp)
