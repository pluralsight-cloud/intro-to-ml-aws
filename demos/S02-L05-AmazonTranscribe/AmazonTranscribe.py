import boto3

client = boto3.client("transcribe")

try:
    response = client.start_transcription_job(
        TranscriptionJobName='TranscribeDemo',
        Media={
            'MediaFileUri': 's3://s3bucketname/prefix/example.mp3'
        },
        LanguageCode='en-AU'
    )

    print(response['TranscriptionJob']['TranscriptionJobStatus'])

except client.exceptions.ConflictException as e:
    job_details = client.get_transcription_job(
        TranscriptionJobName='TranscribeDemo'
    )

    if job_details['TranscriptionJob']['TranscriptionJobStatus'] == "COMPLETED":
        print(job_details['TranscriptionJob']['Transcript']['TranscriptFileUri'])

    else:
        print(job_details['TranscriptionJob']['TranscriptionJobStatus'])