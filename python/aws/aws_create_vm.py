import boto3, os
access_key=os.getenv('AWS_ACCESS_KEY')
secret_key=os.getenv('AWS_SECRET_KEY')
session =boto3.Session(
              aws_access_key_id=access_key,
              aws_secret_access_key=secret_key,
              region_name='us-west-1')

ec2=session.resource('ec2')

instances=ec2.create_instances(
     ImageId='ami-08d4f6bbae664bd41',
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='aws_test',
     NetworkInterfaces=[
        {
            'DeviceIndex':0,
            'Groups':['sg-0df67b937aa940099'],
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            'SubnetId': 'subnet-0323993772c957c4b'
        }
    ]
     )

ec2_id=instances[0].id
print(f"instance_Id=: {ec2_id}")

ec2_client=session.client('ec2')


my_ec2= ec2_client.describe_instances(InstanceIds=[ec2_id])

print(f"Public IP Address: {my_ec2['Reservations'][0]['Instances'][0]['PublicIpAddress']}")
