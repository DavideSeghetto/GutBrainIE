import spacy
import json

# Load your trained SpaCy model
nlp = spacy.load("output/model-best")

# Load evaluation data from a JSON file
#with open("Test_Data/articles_test.json", "r") as f:
with open("Test_Data/articles_test.json", "r") as f:
    evaluation_data = json.load(f)

# Process and collect outputs
results = {}

for doc_id, content in evaluation_data.items():
    entities = []
    for field in ["title", "abstract"]:
        text = content.get(field)
        if not text:
            continue  # Skip if the field is missing or empty
        doc = nlp(text)
        for ent in doc.ents:
            entities.append({
                "start_idx": ent.start_char,
                "end_idx": ent.end_char - 1,
                "location": field,
                "text_span": ent.text,
                "label": ent.label_
            })
    results[doc_id] = {"entities": entities}

# Save results to JSON file
with open("run_test.json", "w") as f:
    json.dump(results, f, indent=4)
