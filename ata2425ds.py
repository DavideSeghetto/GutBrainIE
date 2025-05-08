import json
import spacy
from spacy.tokens import DocBin

def create_doc_bin(all_docs, output_file):
    nlp = spacy.blank("en")  # Empty model for training
    doc_bin = DocBin()
    for doc in all_docs:
        for doc_id, doc_data in doc.items():
            if(doc_id=="36093196"):
                continue
            title = doc_data["metadata"]["title"]
            abstract = doc_data["metadata"]["abstract"]
            full_text = f"{title} {abstract}"
            
            # Crea un documento spaCy
            doc = nlp.make_doc(full_text)
            entities = []
            for ent in doc_data["entities"]:
                if ent["location"] == "title":
                    start = ent["start_idx"]
                    end = ent["end_idx"]
                elif ent["location"] == "abstract":
                    start = len(title) + 1 + ent["start_idx"]
                    end = len(title) + 1 + ent["end_idx"]
                span = doc.char_span(start, end + 1, label=ent["label"])
                if span is None:
                    continue
                entities.append(span)
                
            doc.ents = entities

            
            doc_bin.add(doc)
    doc_bin.to_disk(output_file)

def read_and_create_data(type):
    all_docs = []
    if(type == 'train'):
        train_sets = (('platinum_quality', 'train_platinum.json'), ('gold_quality', 'train_gold.json'), ('silver_quality', 'train_silver.json'), ('bronze_quality', 'train_bronze.json'))
        for quality, file in train_sets:
            path = "Annotations/Train/{quality}/json_format/{file}".format(quality=quality, file=file)
            with open(path, 'r', encoding='utf-8') as f:
                train_data = json.load(f)
                all_docs.append(train_data)
        create_doc_bin(all_docs, 'train.spacy')

    elif(type == 'dev'):
        path = "Annotations/Dev/json_format/dev.json"
        with open(path, 'r', encoding='utf-8') as f:
            dev_data = [json.load(f)]
        create_doc_bin(dev_data, 'dev.spacy')

    else:
        print("Must provide a parameter")

read_and_create_data('train')
read_and_create_data('dev')
print("### Finished ###")