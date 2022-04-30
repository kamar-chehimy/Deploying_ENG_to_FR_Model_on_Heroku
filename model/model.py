import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

import re
import numpy as np
import pickle

import logging

class En_Fre_Translation:

    def __init__(self, model_path):
        logging.info("En_Fre_Translation class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")
    
    def load_text(self, path):
        a_file = open(path, "rb")
        output = pickle.load(a_file)
        return output
    
        
    def translate(self,text,max_seq_length):
        text=re.sub(r'[^\w\s]', '', text)

        en_word_index=self.load_text('en_word_index.txt')
        fr_word_index=self.load_text('fr_word_index.txt')


        sentence = [en_word_index[word] for word in text.split()]
        sentence = pad_sequences([sentence], maxlen=max_seq_length, padding='post')

        result=self.model.predict(sentence[:1])[0]
        index_to_words = {id: word for word, id in fr_word_index.items()}
        index_to_words[0] = '<PAD>'
        result=' '.join([index_to_words[prediction] for prediction in np.argmax(result, 1)])

        result=result.split()

        output=[]
        for i in result:
            if i !='<PAD>':
                output.append(i)

        return (' '.join(output))

def main():
	model = En_Fre_Translation('.\model\En_Fr_Translation.h5')
	predicted_text = model.translate("she is driving the truck",21)
	logging.info( f"This is the translation: \n {predicted_text}") 


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()