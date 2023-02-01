import minio
import json

config_file = open("config.json", "r")
config = json.load(config_file)
config_file.close()
# config from bucket
from_config= config["from_bucket"]
to_config = config["to_bucket"]

from_client = minio.Minio(from_config["endpoint"],
                            access_key=from_config["access_key"],    
                            secret_key=from_config["secret_key"],
                            secure=from_config["secure"])
to_client = minio.Minio(to_config["endpoint"],
                            access_key=to_config["access_key"],
                            secret_key=to_config["secret_key"],
                            secure=to_config["secure"])


# local
minio_client = minio.Minio("127.0.0.1:9000",
                           access_key="minioadmin",
                           secret_key="minioadmin",
                           secure=False)
def migrateBucketFromToBucketTo():
    # get all objects
    objects = minio_client.list_objects(from_config["bucket"], prefix="", recursive=True)
    for obj in objects:
        # get object
        data = minio_client.get_object(from_config["bucket"], obj.object_name)
        print("migrating: " + obj.object_name)
        # put object
        to_client.put_object(to_config["bucket"], obj.object_name, data, obj.size, obj.content_type)

def print_tree(bucket, prefix=""):
    # list all objects in the bucket
    objects = minio_client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        print(obj.object_name)

def main():
    print("migrating from: " + from_config["bucket"] + " to: " + to_config["bucket"])
    migrateBucketFromToBucketTo()

if __name__ == "__main__":
    main()