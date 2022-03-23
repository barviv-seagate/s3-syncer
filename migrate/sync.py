import os
import utils
from subprocess import check_output

def main():
    config = utils.get_config("../config.json")

    source_prefix = ''
    exclude, include = [], []
    region = config["lyvecloud"]["region_name"] #os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    source_bucket = config["aws"]["bucket_name"] #os.getenv('SOURCE_BUCKET', 'aws-bucket')
    target_bucket = config["lyvecloud"]["bucket_name"] #os.getenv('TARGET_BUCKET', 'lyvecloud-bucket')
    endpoint = config["lyvecloud"]["endpoint_url"] #os.getenv('ENDPOINT', 'https://s3.us-east-1.lyvecloud.seagate.com')

    sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} s3://{target_bucket}{source_prefix} --region {region} --endpoint-url {endpoint}'
    if len(exclude) > 0:
        sync_cmd += ' --exclude ' + ' --exclude '.join(exclude)
    if len(include) > 0:
        sync_cmd += ' --include ' + ' --include '.join(include)

    print(f'running {sync_cmd}')
    out = check_output(sync_cmd.split(' '))
    print(f'output:\n {out}')

if __name__ == '__main__':
    main()
