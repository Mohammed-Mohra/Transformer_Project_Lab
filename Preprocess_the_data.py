

import glob
import os
import unicodedata
import string
import numpy
import re
import pandas as pd

import numpy as np
import keras
import string
import time 
import nltk
import gensim, logging

from keras.preprocessing.text import Tokenizer
#from keras_preprocessing.sequence import pad_sequences
import math
string.punctuation = string.punctuation +'“'+'”'+'-'+'’'+'‘'+'—'
string.punctuation = string.punctuation.replace('.', '') #why replace the dot with empty shit. Because we want to get senteneces make senseb

#pathlib.PosixPath
from pathlib import Path

import nltk
nltk.download('punkt')

nltk.download('stopwords')

# load stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))


parent_directory = Path('C:\\University study material\\Project lab\\AUTHORS\\AUTHORS\ARISTOTLE\\')
parent_directory_string = 'C:\\University study material\\Project lab\\AUTHORS\\AUTHORS\ARISTOTLE\\'
total_words = []
file_p = ""
for file_path in parent_directory.iterdir():
    if file_path.is_file() and file_path.suffix == ".txt":
      # Loads the data and preprocesses data and stores corpus in raw_text
      raw_text = open(parent_directory_string + file_path.name, encoding = 'utf8').read()

      file_nl_remo = ""
      for line in raw_text:
        new_line = line.replace("\n", " ")           
      #removes newlines
        file_nl_remo += new_line

      #new_file = new_file.lower()   
      
      file_p += re.sub("[^A-Za-z'.]+", ' ',file_nl_remo).lower()  

      #removes all special characters
      sents = nltk.sent_tokenize(file_p)
      print("The number of sentences is", len(sents)) 
      #prints the number of sentences

      string.punctuation = string.punctuation + '.' # why did we add the dot now 
      file_p = re.sub("[^A-Za-z']+", ' ',file_p).lower()   


      words = nltk.word_tokenize(file_p)
      words = [word for word in words if word not in stop_words]
      unique_tokens = set(words)
      print("The number of unique tokens are", len(unique_tokens)) 
      total_words.append(word for word in words if word not in stop_words)

vocab_size = len(unique_tokens) +10 #chosen based on statistics of the model

oov_tok = '<OOV>'
padding_type='post'
trunc_type='post'
# tokenizes sentences
tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts([file_p])
word_index = tokenizer.word_index
seq_length = 50
tokens = tokenizer.texts_to_sequences([file_p])[0]

from gensim.models import KeyedVectors

# Load the pre-trained Word2Vec model

embedding_file = 'word2vec-google-news-300.model.vectors.npy'
embedding_matrix = np.load("C:\\University study material\\Project lab\\LSTM on Aristotle\\" + embedding_file)

dataX = []
dataY = []

seq_length = 50

for i in range(0, len(tokens) - seq_length-1 ):
    seq_in = tokens[i:i + seq_length] # The 50 word sequence
    seq_out = tokens[i + seq_length] # The word that we want to predict 

    if seq_out==1: #Skip samples where target word is OOV
        continue
    
    dataX.append(seq_in)
    dataY.append(seq_out)

X = numpy.array(dataX)
Y = numpy.array(dataY)

numpy.save("Xdata_npy", X, allow_pickle=True, fix_imports=True)
numpy.save("Ydata_npy", y, allow_pickle=True, fix_imports=True)