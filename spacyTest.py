import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

doc = nlp("My name is Ron and I was born on April 17, 1989. I am currently working at Teleperformance as a customer service representative since September 25th last year.")
for ent in doc.ents:
    print(ent.text, ent.label_)
