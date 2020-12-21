import botocore
import logging
import sonrai.platform.aws.arn


def run(ctx):
    
    resource_arn = sonrai.platform.aws.arn.parse(ctx.resource_id)
    resource = resource_arn.  \
        .assert_service("ec2") \
        .assert_type("instance") \
        .resource

    ec2_client = ctx.get_client().get('ec2', resource_arn.region)


    print(resource_arn)

    # Create ec2 client 
    response = ec2_client.describe_instances()
    

    print(response)