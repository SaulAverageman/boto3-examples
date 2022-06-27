import boto3
client=boto3.client('ec2')

resp=client.terminate_instances(InstanceIds=['i-0055f8f7d88360fc9'])
for ins in resp['TerminatingInstances']:
	print(ins['InstanceId']+" terminated")