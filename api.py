import paralleldots

paralleldots.set_api_key("1eded93dd7e9fa44d4b205d2f36734f65a5a141c")

def ner(text):
    ner = paralleldots.ner(text)
    return ner