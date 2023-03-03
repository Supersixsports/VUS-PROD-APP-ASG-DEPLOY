
import requests
import boto3
import time


autoscaling = boto3.client('autoscaling',
                                region_name='ap-south1')

ec2 = boto3.client('ec2',
                   region_name='ap-south-1'
                   )
def launch_template(ami):
    response = ec2.create_launch_template(
        LaunchTemplateName='{templatename}'.format(templatename='VUS-PROD-APP'),
        LaunchTemplateData={
            'IamInstanceProfile': {
                'Name': 'EC2-role-cloudwatch'
            },
            'ImageId': '{ami_id}'.format(ami_id=ami),
            'InstanceType': 'm6a.large',
            'KeyName': 'devops',
            'SecurityGroupIds': ['sg-0341e3f719c9604b9']
            #'UserData': userdata
        })
    return response

def update_autoscaling(template_name):
    response = autoscaling.update_auto_scaling_group(
        AutoScalingGroupName='VUS-PROD-APP',
        LaunchTemplate={
            'LaunchTemplateName': '{template}'.format(template=template_name)
            }
         )
    return response

def instance_refresh():
    response = autoscaling.start_instance_refresh(AutoScalingGroupName='VUS-PROD-APP')
    return response


