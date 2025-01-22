import boto3, os

access_key=os.getenv('AWS_ACCESS_KEY')
secret_key=os.getenv('AWS_SECRET_KEY')

session=boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name='us-west-1')

ec2=session.resource('ec2')
instances=ec2.instances.filter()

for instance in instances:
    print(instance.id)
