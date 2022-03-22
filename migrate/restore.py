import os
import utils

def main():
    source_prefix = ''
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    source_folder = os.getenv('SOURCE_FOLDER', 'aws-bucket')
    target_bucket = os.getenv('TARGET_BUCKET', 'lyvecloud-bucket')
    endpoint = os.getenv('ENDPOINT', 'https://s3.us-east-1.lyvecloud.seagate.com')
    sync_cmd = f'aws s3 sync {source_folder} s3://{target_bucket}{source_prefix} --region {region} --endpoint-url {endpoint}'
    utils.run_cmd(sync_cmd)

if __name__ == '__main__':
    main()
