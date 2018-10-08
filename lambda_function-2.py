import boto3


rekognition = boto3.client('rekognition')
dynamodb = boto3.client('dynamodb')
s3 = boto3.client('s3') 

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
        
    #bucket = "face-rekog-test"
    #key = "12.jpg"
        
    response = rekognition.search_faces_by_image(
            CollectionId='family_collection',
            Image={"S3Object":
                 {"Bucket": bucket,
                 "Name": key}}                                     
            )
    #print (response['FaceMatches'])
    for match in response['FaceMatches']:
        #print (match['Face']['FaceId'],match['Face']['Confidence'])
            
        face = dynamodb.get_item(
            TableName='family_collection',  
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
            )
        
        if 'Item' in face:
            final = face['Item']['FullName']['S']
            Valid = face['Item']['RekognitionId']['S']
            break
            
            
        else:
            print ('no match found in person lookup')
            
    print(final)
    Valid = "1"
    print(Valid)
    response = dynamodb.put_item(
        TableName="Face_rekog",
        Item={
            'ID': {'S': Valid},
            'bucket': {'S': bucket},
            'key': {'S': key},
            'FullName': {'S': final}
            }
        ) 
            
            
            