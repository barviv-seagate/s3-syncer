import os
import utils

def main():
    source_prefix = ''
    target_folder = os.getenv('TARGET_FOLDER', './data')
    region = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    source_bucket = os.getenv('SOURCE_BUCKET', 'aws-bucket')
    sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} {target_folder} --region {region}'
    utils.run_cmd(sync_cmd)

if __name__ == '__main__':
    main()