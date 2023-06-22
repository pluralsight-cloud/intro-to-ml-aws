import boto3

client = boto3.client("translate")

response = client.translate_text(
    Text="Keep being awesome, cloud gurus!",
    SourceLanguageCode="en",
    TargetLanguageCode="hi"
)

print(response["TranslatedText"])