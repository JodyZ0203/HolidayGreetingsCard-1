'''
Using machine learning to aid the diagnosis of COVID-19 in patients.
Author: Batuhan Aktan, Jody Zhou, Sam  ...
Date: DEC 2020
'''
from tensorflow.keras.models import Sequential
from keras.layers import *
import numpy as np
from keras.utils import np_utils
import pickle

f = open("Greetings.txt", encoding="utf8")
content = f.read()
chars = sorted(list(set(content)))


numCharMap = {n:character for n, character in enumerate(chars)}
charNumMap = {character:n for n, character in enumerate(chars)}

length = len(content)
seqLen = 10
X = []
y = []

for i in range (0,length-seqLen,1):
    seq = content[i:i + seqLen]
    label = content[i+seqLen]
    X.append([charNumMap[char] for char in seq])
    y.append(charNumMap[label])


X = np.reshape(X, (len(X), seqLen, 1))
X = X/float(len(chars))
y = np_utils.to_categorical(y)


model = Sequential()
model.add(LSTM(400, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(400))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.save('TextModel.h5')
#############################
string_mapped = list(X[99])
full_string = [numCharMap[value[0]*72] for value in string_mapped]


for i in range(400):
    X = np.reshape(string_mapped,(1,len(string_mapped), 1))
    X = X / float(len(chars))

    pred_index = np.argmax(model.predict(X, verbose=1))
    seq = [numCharMap[value[0]*72] for value in string_mapped]
    full_string.append(numCharMap[pred_index])
    string_mapped.append(pred_index)
    string_mapped = string_mapped[1:len(string_mapped)]

txt = ""
for char in full_string:
    txt = txt+char
print(txt)

#############################
pickleOut = open("X.pickle", "wb")
pickle.dump(X, pickleOut)
pickleOut.close()

pickleOut = open("y.pickle", "wb")
pickle.dump(y, pickleOut)
pickleOut.close()

pickleOut = open("numChar.pickle", "wb")
pickle.dump(numCharMap, pickleOut)
pickleOut.close()

