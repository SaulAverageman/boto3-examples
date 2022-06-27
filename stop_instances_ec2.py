import boto3
client=boto3.client('ec2')
client.stop_instances(InstanceIds=['i-061cbbc5ffee70e80'])
