import boto3
import os
from botocore.config import Config

env = dict(map(lambda x: tuple(x.split("=")),open('.env').read().split("\n"))) if os.path.exists(".env") else os.environ

my_config = Config(
    region_name='ru-central-1',
)


session = boto3.session.Session()
s3 = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_secret_access_key=env['AWS_SECRET_ACCESS_KEY'],
    aws_access_key_id=env['AWS_ACCESS_KEY_ID'],
    config=my_config
)
os.makedirs(env['TARGET_DIR'], exist_ok=True)
for key in filter(lambda x: x["Key"].startswith(env["PROJECT_NAME"]) and x["Size"], s3.list_objects(Bucket='mods-bucket')['Contents']):
    resp = s3.get_object(Bucket='mods-bucket',Key=key["Key"])
    open(env["TARGET_DIR"] + (key["Key"].lstrip(env["PROJECT_NAME"])), "wb").write(resp["Body"].read())