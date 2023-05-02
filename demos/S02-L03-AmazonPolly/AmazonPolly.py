from contextlib import closing
import boto3

client = boto3.client("polly")

response = client.synthesize_speech(
    Text='Hi, my name is Joanna, and I\'m being invoked by the AWS SDK',
    VoiceId='Joanna',
    Engine='neural',
    OutputFormat='mp3'
)

with closing(response["AudioStream"]) as stream:
    with open("polly-py.mp3", "wb") as file:
        file.write(stream.read())