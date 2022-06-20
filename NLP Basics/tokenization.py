#Importing libraries
import spacy

nlp = spacy.blank("en")
doc = nlp("Hello World, I am Amit Joshi!")

for token in doc:
    print(token)

