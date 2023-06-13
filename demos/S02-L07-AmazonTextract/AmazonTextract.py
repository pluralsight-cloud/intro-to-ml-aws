import boto3

client = boto3.client("textract")

response = client.analyze_id(
    DocumentPages=[{
        'S3Object': {
            'Bucket': 'textract-console-us-east-1-b75fd75d-6118-48bc-a874-cc552907bd68',
            'Name': 'uploads/id/ExampleDriversLicense.jpg'
        }
    }]
)

id_values = dict()

for field in response['IdentityDocuments'][0]['IdentityDocumentFields']:
    id_values[ field['Type']['Text'] ] = field['ValueDetection']['Text']

print("Type: {} - Ref #{}"
        .format(
            id_values['ID_TYPE'],
            id_values['DOCUMENT_NUMBER']
        )
    )
print("{}, {} {}"
        .format(
            id_values['LAST_NAME'],
            id_values['FIRST_NAME'],
            id_values['MIDDLE_NAME']
        )
    )

### Output
# Type: DRIVER LICENSE FRONT - Ref #X013207832
# CLOUDWORTH, CASEY