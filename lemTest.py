import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

# Ensure required resources are downloaded
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to convert POS tag to WordNet POS tag
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Example text
text = "I went to manila and will go to Bagiuo."
tokens = word_tokenize(text)
tagged_tokens = nltk.pos_tag(tokens)

# Lemmatize each token with its POS tag
lemmatized = [lemmatizer.lemmatize(token, get_wordnet_pos(pos)) for token, pos in tagged_tokens]

print("Tokens:", tokens)
print("Lemmatized:", lemmatized)
