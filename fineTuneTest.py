from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')
response = generator("Eringz is here to help you with", max_length=50, num_return_sequences=1, truncation=True)
print(response)
