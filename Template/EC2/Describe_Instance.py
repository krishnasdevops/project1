import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
for r in response['Reservations']:
  for i in r['Instances']:
    print (i['InstanceId'],i['ImageId'])
    for b in i['BlockDeviceMappings']:
      print (b['Ebs']['DeleteOnTermination'])
      # for a in i['Placement']:
      #   print(a['AvailabilityZone'])