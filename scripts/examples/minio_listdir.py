import envutils
import os
from minio import Minio
from pyminio import Pyminio

MINIO_HOSTNAME=os.getenv("MINIO_HOSTNAME")
MINIO_ACCESSKEY=os.getenv("MINIO_ACCESSKEY")
MINIO_SECRETKEY=os.getenv("MINIO_SECRETKEY")
MINIO_BUCKET=os.getenv("MINIO_BUCKET")


minio_obj = Minio(
    endpoint=MINIO_HOSTNAME,  # e.g. "localhost:9000/"
    access_key=MINIO_ACCESSKEY,
    secret_key=MINIO_SECRETKEY,
    secure=False
)
# minio_obj.list_buckets()
pyminio_client = Pyminio(minio_obj=minio_obj)
output_list = pyminio_client.listdir(os.path.join(MINIO_BUCKET, ""))
# print(output_list)

for root_dir, dirpath, filenames in pyminio_client.walk(os.path.join(MINIO_BUCKET, "")):
    print(root_dir, dirpath, filenames)