import spacy

nlp = spacy.load("en_core_web_sm")

def ner(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append({
            'name': ent.text,
            'category': ent.label_
        })
    return {'entities': entities}