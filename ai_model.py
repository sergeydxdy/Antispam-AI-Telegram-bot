from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class Model:
    def __init__(self):
        self.model_path = "H:\\Coding\\spam_deberta_v4"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_path)

    def predict_spam(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class = torch.argmax(logits, dim=1).item()
        return predicted_class == 1
