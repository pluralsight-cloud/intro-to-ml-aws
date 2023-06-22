import boto3

client = boto3.client("comprehend")

response = client.detect_targeted_sentiment(
    Text="The burgers were terrible, but the manager was super helpful",
    LanguageCode="en"
)

for entity in response["Entities"]:
    result = entity["Mentions"][0]

    print("{} ({})".format( result["Text"], result["Type"] ))
    print(result["MentionSentiment"]["Sentiment"])
    print()
