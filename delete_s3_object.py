import boto3
client=boto3.client('s3')
=
response=client.delete_object(ACL='private',
		Body=file,
		Bucket='bba62679834076',
		Key='text.txt')
