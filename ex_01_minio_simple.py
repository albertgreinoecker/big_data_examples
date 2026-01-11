import boto3

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:9000",
    aws_access_key_id="minioadmin",
    aws_secret_access_key="minioadmin",
    region_name="eu-central-1"
)
#s3.create_bucket(Bucket="test-bucket")

s3.put_bucket_versioning(
    Bucket="test-bucket",
    VersioningConfiguration={"Status": "Enabled"}
)

s3.upload_file(
    "data/f1.txt",          # lokale Datei
    "test-bucket",        # Bucket
    "f1.txt"   # Objektname in MinIO
)

s3.upload_file(
    Filename= "data/f1.txt",
    Bucket="test-bucket",
    Key="f1_meta.txt",
    ExtraArgs={
        "Metadata": {
            "author": "hubert",
            "project": "uni",
            "version": "1"
        }
    }
)

s3.put_object(
    Bucket="test-bucket",
    Key="direct_text.txt",
    Body=b"This is a direct text upload to MinIO.\n"
)

s3.put_object(
    Bucket="test-bucket",
    Key="direct_text_metadata.txt",
    Body=b"Version 1",
    Metadata={
        "author": "hubert",
        "project": "uni"
    }
)

############################################
# retrieve and update metadata, then re-upload

obj = s3.get_object(
    Bucket="test-bucket",
    Key="direct_text.txt"
)

data = obj["Body"].read()

s3.put_object(
    Bucket="test-bucket",
    Key="direct_text.txt",
    Body=data,
    Metadata={
        "author": "hubert",
        "project": "uni",
        "status": "reviewed"
    }
)

############################################
# Delete Object


# Without versioning, object is simply deleted
s3.delete_object(
    Bucket="test-bucket",
    Key="direct_text.txt"
)


# With versioning, a delete marker is created
s3.delete_object(
    Bucket="test-bucket",
    Key="direct_text.txt"
)

# To permanently delete, need to specify version ID
s3.delete_object(
    Bucket="test-bucket",
    Key="direct_text.txt",
    VersionId="VERSION_ID_HIER"
)

# List all Versions of an Object
resp = s3.list_object_versions(Bucket="test-bucket")

for v in resp.get("Versions", []):
    print("KEY", v["Key"], "VERSION:", v["VersionId"], "LATEST:", v["IsLatest"])
