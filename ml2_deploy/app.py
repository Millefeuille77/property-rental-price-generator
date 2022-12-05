from codecs import latin_1_decode
# Import Libraries
import streamlit as st
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing import text, sequence

model = tf.keras.models.load_model('model_seq_news.h5')
stpwds_en = pickle.load(open('stpwds_en.pkl', 'rb'))
stop = pickle.load(open('stop.pkl', 'rb'))

st.header('Fake News Detector')

news = st.text_input("input the news here")

if st.button('submit'):
    max_len = 16799
    tokenizer = text.Tokenizer()
    tokenized = tokenizer.texts_to_sequences(news)
    news_pad = sequence.pad_sequences(tokenized,maxlen=max_len) #val tokenize data
  
    pred = model.predict(news_pad)
    if pred[0][0] <= 0.5:
        st.text('The news is fake')
    else:
        st.text('The news is true')

  
