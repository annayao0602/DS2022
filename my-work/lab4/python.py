#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

import urllib.request
import boto3
import ssl
import certifi

bucket_name = 'ds2022-zzz2bx'
file_name = 'hamster.jpg'
url = 'https://cdn.britannica.com/57/192357-050-62E912BD/hamster-Syria-households-pet.jpg'
context = ssl.create_default_context(cafile=certifi.where())

response = urllib.request.urlopen(url, context=context)
file_data = response.read()

s3 = boto3.client('s3', region_name='us-east-1')

resp = s3.put_object(
    Body=file_data,
    Bucket=bucket_name,
    Key=file_name
)

expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': file_name},
    ExpiresIn=expires_in
)

print("Presigned URL:", response)
# Presigned URL: https://ds2022-zzz2bx.s3.amazonaws.com/hamster.jpg?AWSAccessKeyId=AKIA2OAJTVODZSWX2RE4&Signature=uR16IJv67kSCicZvyeEFcfWdXJs%3D&Expires=1728327133
