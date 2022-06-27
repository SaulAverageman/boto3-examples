import boto3
clt=boto3.client('ec2')
resp=clt.run_instances(ImageId='ami-0e1d30f2c40c4c701', InstanceType='t2.micro', MinCount=1, MaxCount=1)
for i in resp['Instances']:
	print(i['InstanceId'])