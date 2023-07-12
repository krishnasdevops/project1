import boto3
#create a boto3 python code to CREATE EC2 Instance  with specified image ID.

def call():
    session = boto3.Session(
    aws_access_key_id='AKIATS7YLYJSKXROIMXP',
    # aws_access_key_id=a,
    aws_secret_access_key='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',  
    # aws_secret_access_key=b,
    )

    ec2 = session.resource('ec2')
    instance = ec2.create_instances(
                                        ImageId='ami-03a933af70fa97ad2',
                                        InstanceType='t2.micro',
                                        MaxCount=1,
                                        MinCount=1,
                                        KeyName='django',
                                        SecurityGroupIds=['sg-0f9255eb2f9d83bbf'],
                                        )
     