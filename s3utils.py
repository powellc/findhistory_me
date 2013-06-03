from storages.backends.s3boto import S3Storage

StaticS3BotoStorage = lambda: S3Storage(location='static')
MediaS3BotoStorage = lambda: S3Storage(location='media')