# Detect Labels from a local image with Amazon Rekognition.

import boto3

client = boto3.client('rekognition')

img = open('demo-rekognitionlabels.png', 'rb')

response = client.detect_labels(Image={'Bytes': img.read()})

for label in response['Labels']:
    # Print the label with the name and confidence percentage (limited to two decimal places) on the same line
    print(label['Name'] + ': ' + str(round(label['Confidence'], 2)) + '%')

img.close()