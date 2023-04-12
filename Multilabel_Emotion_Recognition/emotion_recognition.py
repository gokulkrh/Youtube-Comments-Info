import pandas as pd
import numpy as np
import keras
from keras.models import load_model
import keras.backend as K
from transformers import BertTokenizerFast, BertConfig
from Preprocessing.emotionrecognizer_process import preprocess_corpus_for_emo


def proba_to_labels(y_pred_proba, threshold=0.8):
    
    y_pred_labels = np.zeros_like(y_pred_proba)
    
    for i in range(y_pred_proba.shape[0]):
        for j in range(y_pred_proba.shape[1]):
            if y_pred_proba[i][j] > threshold:
                y_pred_labels[i][j] = 1
            else:
                y_pred_labels[i][j] = 0
                
    return y_pred_labels


def emotion_recognizer(text_samples):
    def get_weighted_loss(weights):
        def weighted_loss(y_true, y_pred):
            return K.mean((weights[:,0]**(1-y_true))*(weights[:,1]**(y_true))*K.binary_crossentropy(y_true, y_pred), axis=-1)
        return weighted_loss

    with keras.utils.custom_object_scope({'weighted_loss': get_weighted_loss}):
        model = load_model('Multilabel_Emotion_Recognition/emotion_recognizer')

    threshold = 0.8700000000000001
    
    text_samples_clean = [preprocess_corpus_for_emo(text) for text in text_samples]

    model_name = 'bert-base-uncased'
    config = BertConfig.from_pretrained(model_name, output_hidden_states=False)
    tokenizer = BertTokenizerFast.from_pretrained(pretrained_model_name_or_path = model_name, config = config)
    
    samples_token = tokenizer(
        text = text_samples_clean,
        add_special_tokens = True,
        max_length = 48,
        truncation = True,
        padding = 'max_length', 
        return_tensors = 'tf',
        return_token_type_ids = True,
        return_attention_mask = True,
        verbose = True,
    )
    
    samples = {'input_ids': samples_token['input_ids'],
               'attention_mask': samples_token['attention_mask'],
               'token_type_ids': samples_token['token_type_ids']
              }
    
    samples_pred_proba = model.predict(samples)
    
    samples_pred_labels = proba_to_labels(samples_pred_proba, threshold)
            
    samples_pred_labels_df = pd.DataFrame(samples_pred_labels)
    emos = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise']
    samples_pred_labels_df = samples_pred_labels_df.apply(lambda x: [emos[i] for i in range(len(x)) if x[i]==1], axis=1)
    
    return pd.DataFrame({"Text":text_samples, "Emotions":list(samples_pred_labels_df)})
