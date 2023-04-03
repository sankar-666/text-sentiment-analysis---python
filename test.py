import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the pre-trained BERT model and tokenizer
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=7)
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Fine-tune the BERT model on an emotion classification dataset

# Classify a new text input
def preddictEmotion(text):
    # text = "I'm feeling really happy today!"
    tokens = tokenizer.encode_plus(text, add_special_tokens=True, max_length=128, padding='max_length', truncation=True, return_tensors='pt')
    input_ids = tokens['input_ids']
    attention_mask = tokens['attention_mask']
    outputs = model(input_ids, attention_mask)
    probs = torch.softmax(outputs.logits, dim=-1)
    emotion_idx = torch.argmax(probs, dim=-1)
    emotion_labels = ['anger', 'disgust', 'fear', 'joy', 'neutral', 'sadness', 'surprise']
    predicted_emotion = emotion_labels[emotion_idx]
    print(f"Predicted emotion: {predicted_emotion}")
    return predicted_emotion

# preddictEmotion("i lost him")