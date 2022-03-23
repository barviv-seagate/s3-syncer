import json

def get_config(file_path):
    with open(file_path, 'r') as file:
        content_json = json.loads(file.read())

    return content_json