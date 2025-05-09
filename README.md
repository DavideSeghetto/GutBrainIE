# GutBrainIE 2025 - Task 6.1 (NER)

This repository contains the system developed for **Task 6.1 (Named Entity Recognition)** of the **BioASQ @ CLEF 2025** challenge.

## 📄 Reproducibility

In order to obtain the final predictions for the test set, you have to follow three small steps.

### 1. Data Extraction & Conversion

The script `ata2425ds.py` is used to:
- Extract annotated data from the official training set.
- Convert the data into `.spacy` format, which is required for training with spaCy.

In order to successfully run the script remember to add the Annotations and the Articles of the training set and dev set in the folder, or alternatively modify the path to your data in the script.

### 2. Model Training

The NER model is trained using [spaCy](https://spacy.io/) with the following command:

```bash
python -m spacy train config_best.cfg --output output --paths.train train.spacy --paths.dev dev.spacy
```

After training, the best-performing model is available in: `output/model-best`

### 3. Submission Generation
The script `submission.py` loads the trained model from `output/model-best` and uses it to produce predictions on test data in the format required by the GutBrainIE 2025 Task 6.1 evaluation system.

In order to successfully run the script remember to add the Test_Data in the folder, or alternatively modify the path to your data in the script.

## 📌 Requirements

- Python 3.8+
- spaCy >= 3.0
- en_core_web_lg spaCy model

Install the required dependencies with:

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_lg
```