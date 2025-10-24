import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello Ron! How's it going? Learning NLP is fun."
words = word_tokenize(text)
sentences = sent_tokenize(text)

print("Words:", words)
print("Sentences:", sentences)
