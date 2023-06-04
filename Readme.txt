#Heading
Hey there!


word2vec-google-news-300.model.vectors: is an embedding matrix to embedd the tokens into 300 dimensional vectors

Aristotle: is a folder that contains all the raw text used to feed the transformer

Preprocess_the_data.py:  The first file you should run. Please change the directory to loop over Aristotle directory. The file will create Xdata_npy.npy and Ydata_npy.npy
  Xdata_npy.npy: is the preprocessed text with sequence length = 50. The data will be imported in a numpy array
  so we need to change the type to tensor after importing 
  
  Ydata_npy.npy: is the preprocessed output text. The data will be imported in a numpy array
  so we need to change the type to tensor after importing 


Transformers from scratch.py: Please run this file after running "Preprocess_the_data.py". It trains the data after it has been preprocessed.
