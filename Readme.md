
# Hey there!

# Introduction 
The goal of this project is to capture the patterns and structure of language, enabling a system to generate coherent and contextually appropriate text.
In this project, a statistical model is trained on a large corpus of text, everything Aristotle wrote which amounts to 500 thousand tokens, to learn the relationships between words and the likelihood of different word sequences occurring. My project is trained using supervised learning techniques, where the model is fed with input
sequences and learns to predict the next word(s) in the sequence. The training data consists of pairs of input sequences and their corresponding target sequences, where the target is the next word or words.
Once the model is trained, it can be used for text generation: Given a starting sequence, the language model can generate coherent and contextually relevant text by predicting the most likely subsequent words.

# How It Works
- # Preporcess the data
    We start by looping over text files in the Aristotle directory, tokenize the text then change it to vectors
    You should run Preprocess_the_data.py first. It will generate Xdata_npy.npy and Ydata_npy.npy array
   
- # Embedding the data and training the model
   Make sure to download from [word2vec-google-news-300.model](https://huggingface.co/fse/word2vec-google-news-300) so you can embedd your tensors.
   After you processed the data. you should run the "Transformers from scratch.py" train the model and get yourself some nice charts for the loss function.  
 
 - # Results
    My resutls looked something like this. I used MSELoss but your free to change in your code to any other loss function 
    (MSELoss.png.jpg)

Preprocess_the_data.py:  The first file you should run. Please change the directory to loop over Aristotle directory. The file will create Xdata_npy.npy and Ydata_npy.npy
  Xdata_npy.npy: is the preprocessed text with sequence length = 50. The data will be imported in a numpy array
  so we need to change the type to tensor after importing 
  
  Ydata_npy.npy: is the preprocessed output text. The data will be imported in a numpy array
  so we need to change the type to tensor after importing 


Transformers from scratch.py: Please run this file after running "Preprocess_the_data.py". It trains the data after it has been preprocessed.
