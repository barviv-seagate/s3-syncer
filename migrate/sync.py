import os
import utils

def main():
    source_prefix = ''
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    source_bucket = os.getenv('SOURCE_BUCKET', 'aws-bucket')
    target_bucket = os.getenv('TARGET_BUCKET', 'lyvecloud-bucket')
    endpoint = os.getenv('ENDPOINT', 'https://s3.us-east-1.lyvecloud.seagate.com')
    sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} s3://{target_bucket}{source_prefix} --region {region} --endpoint-url {endpoint}'
    utils.run_cmd(sync_cmd)

if __name__ == '__main__':
    main()
