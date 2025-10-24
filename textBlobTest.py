from textblob import TextBlob

text = "I am happy"
blob = TextBlob(text)
print(blob.sentiment)