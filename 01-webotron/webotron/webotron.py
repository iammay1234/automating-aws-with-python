import boto3
import click #use this instead of sys module as a better way to manage passing arguments to cli

#click module will automatically generate a help menu

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

#the @click is a decorator
@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

#the group decortor to help grouping commands where the main group will be calll directly as a wrapper
@cli.command('list-buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
#use click Arguments feature to pass in bucket name
@click.argument('bucket')
def list_bucket_objects(bucket):
    "list objects in an s3 object"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)



if __name__ == '__main__':
        #list_buckets()
        cli()
