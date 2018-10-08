import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('51.jpg','Annie Johnson'),
        ('52.jpg','Annie Johnson'),
        ('53.jpg','Annie Johnson'),
        ('54.jpg','Annie Johnson'),
        ('55.jpg','Annie Johnson'),
        ('56.jpg','Annie Johnson'),
        ('57.jpg','Annie Johnson'),
        ('58.jpg','Annie Johnson'),
        ('59.jpg','Annie Johnson'),
        ('60.jpg','Annie Johnson'),
        ('61.jpg','Annie Johnson'),
        ('62.jpg','Annie Johnson'),
        ('63.jpg','Annie Johnson'),
        ('64.jpg','Annie Johnson'),
        ('65.jpg','Annie Johnson'),
        ('66.jpg','Annie Johnson'),
        ('67.jpg','Annie Johnson'),
        ('68.jpg','Annie Johnson'),
        ('69.jpg','Annie Johnson'),
        ('70.jpg','Annie Johnson'),
        ('71.jpg','Annie Johnson'),
        ('72.jpg','Annie Johnson'),
        ('73.jpg','Annie Johnson'),
        ('74.jpg','Annie Johnson'),
        ('75.jpg','Annie Johnson')
        ]

# Iterate through list to upload objects to S3
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('rekognition-pictures-sample1998','index/'+ image[0])
    ret = object.put(Body=file,
                     Metadata={'FullName':image[1]}
                     )
