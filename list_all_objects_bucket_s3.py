import boto3
client=boto3.client('s3')
response=client.list_objects(Bucket='meanbucketmemme')
for c in response['Contents']:
	print(c['Key'])
