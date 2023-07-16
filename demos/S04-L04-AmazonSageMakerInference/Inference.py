import boto3

client = boto3.client('runtime.sagemaker')

img = open('demo-rekognitionlabels.png', 'rb').read()

response = client.invoke_endpoint(
    EndpointName = 'ssennett-introtoml-endpoint',
    Body = img,
    ContentType = 'application/x-image',
    Accept = 'application/json;verbose'
)

print(response)