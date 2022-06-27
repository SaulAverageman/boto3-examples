import boto3
client=boto3.client('s3')
file=open(r'text.txt').read()
response=client.put_object(ACL='public',
		Body=file,
		Bucket='meanbucketmemme',
		Key='random')
