import boto3
client=boto3.client('s3')

response=client.create_bucket(ACL='private', Bucket='bba62679834076', CreateBucketConfiguration={
			'LocationConstraint':'ap-south-1'}
)
