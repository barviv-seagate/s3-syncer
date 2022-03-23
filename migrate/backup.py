import os
import utils
from subprocess import check_output

def main():
    config = utils.get_config("../config.json")

    source_prefix = ''
    exclude, include = [], []
    target_folder = config["aws"]["target_folder"] #os.getenv('TARGET_FOLDER', './data')
    region = config["aws"]["region_name"] #os.getenv('AWS_DEFAULT_REGION', 'us-east-1')
    source_bucket = config["aws"]["bucket_name"] #os.getenv('SOURCE_BUCKET', 'aws-bucket')

    sync_cmd = f'aws s3 sync s3://{source_bucket}{source_prefix} {target_folder} --region {region}'
    if len(exclude) > 0:
        sync_cmd += ' --exclude ' + ' --exclude '.join(exclude)
    if len(include) > 0:
        sync_cmd += ' --include ' + ' --include '.join(include)

    print(f'running {sync_cmd}')
    out = check_output(sync_cmd.split(' '))
    print(f'output:\n {out}')

if __name__ == '__main__':
    main()
