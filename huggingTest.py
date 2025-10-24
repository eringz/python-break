from transformers import pipeline

sentiment_analyzer = pipeline('sentiment-analysis')
result = sentiment_analyzer("I strongly don't love learning with Eringz!")
print(result)