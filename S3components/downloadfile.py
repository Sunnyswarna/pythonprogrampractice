import boto3
s3 = boto3.client('s3')
s3.download_file('amzn-s3-demo-bucket', 'hello.txt', '/tmp/hello.txt')