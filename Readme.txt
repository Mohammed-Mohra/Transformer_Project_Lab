Hey there!

word2vec-google-news-300.model.vectors: is an embedding matrix to embedd the tokens into 300 dimensional vectors

Xdata_npy.npy: is the preprocessed text with sequence length = 50. The data will be imported in a numpy array
so we need to change the type to tensor after importing 

Ydata_npy.npy: is the preprocessed output text. The data will be imported in a numpy array
so we need to change the type to tensor after importing 

Aristotle: is a folder that contains all the raw text used to feed the transformer

preprcocess_the_data.py: taking raw data and saving them as a numpy array for later use 

Transformers from scratch.py: Trains the data after it has been preprocessed.
