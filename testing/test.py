
import pickle, json
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing import sequence
from tensorflow import keras

with open('../ToSite/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

data = [60,11000.0,1,
            "A graphic novel and unique take on Anthology Horror. This volume would tell a single story, and introduce it's host, The Gravedigger!",
            66]
df = pd.DataFrame(data=[data])

maxlen = 43 # Somewhat arbitrary at this point, neccessary however
seq = tokenizer.texts_to_sequences(df[3])
 # seq2 = [i for s in seq for i in s]
padded_sequence = sequence.pad_sequences(seq, maxlen)
# Convert text to df columns (inelegant, but effective)
for j in range(5, 48):
    f = j-5
    df[j] = [padded_sequence[0][f]]
# Drop unencoded text column
df.drop(columns=[3], inplace=True)
# Convert df to numpy array, for further conversion to tensor
arr = df.to_numpy()
print(arr)  # DEV, delete before prod
# Reshape array into tensor
tarr = arr.reshape(1, 47, 1)
tarr = np.asarray(tarr).astype('float32')
# Loading in the model
model = keras.models.load_model('../ToSite/models')
print(model.summary())
print(arr.shape)
# Formatting output from the model
y_pred_proba = round((model.predict(tarr)[0][0] * 100), 2)

print(y_pred_proba)

exit()