import botocore


def run(ctx):
    # Create ec2 client 
    client = ctx.get_client().get('ec2')
    
    response = client.describe_instances()
    

    print(response)