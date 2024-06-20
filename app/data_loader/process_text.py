import spacy

nlp = spacy.load("en_core_web_sm")

def extract_relevant_info(text):
    doc = nlp(text)
    prompts = []
    for sent in doc.sents:
        if "character creation" in sent.text.lower() or "attribute" in sent.text.lower():
            prompts.append(sent.text)
    return prompts
