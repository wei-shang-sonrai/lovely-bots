import botocore
import sonrai.platform.aws.arn

def run(ctx):

    print("hello world!")


    resource_id = ctx.resource_id
    resource_arn = sonrai.platform.aws.arn.parse(resource_id)

    print(resource_id)

    print(resource_arn)

    # Create ec2 client 
    client = ctx.get_client().get('ec2')
    
    response = client.describe_instances()
    

    print(response)