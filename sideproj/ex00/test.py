import numpy as np
import pandas as pd
import keras
import sklearn
from keras.datasets import mnist
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

import os

print("Library imports succesful")

#Paramètres
batch_size =32
num_classes=10
epochs = 10

#import MNIST
(x_trainraw, y_train), (x_testraw, y_test) = mnist.load_data()

print("MNIST import succesful")


#add a column of 1 to x_train et x_test
x_train=np.zeros((x_trainraw.shape[0],28,28,1))
x_train[:,:,:,0]=x_trainraw
x_test=np.zeros((x_testraw.shape[0],28,28,1))
x_test[:,:,:,0]=x_testraw

print(x_train.shape, y_train.shape)
print(x_test.shape, y_test.shape)

from sklearn.model_selection import train_test_split
x_test, x_controle, y_test, y_controle = train_test_split(x_test, y_test, test_size=0.1)

x_test.shape, y_test.shape



#On ne redimensionne plus puisqu'on va prendre une convolution en 2D
#x_train=x_train.reshape(60000,28**2)
#x_test=x_test.reshape(10000,28**2)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
# ne pas recalculer
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
y_controle = keras.utils.to_categorical(y_controle, num_classes)

x_train.shape[1:], x_controle.shape

monmodele = Sequential()
monmodele.add(Conv2D(28, (3,3), padding='same', input_shape=x_train.shape[1:]))
monmodele.add(Activation('relu'))
monmodele.add(Conv2D(16, (3, 3)))
monmodele.add(Activation('relu'))

monmodele.add(MaxPooling2D(pool_size=(2, 2)))
monmodele.add(Dropout(0.25))

monmodele.add(Flatten())

monmodele.add(Dense(32,activation='relu'))
monmodele.add(Dense(16,activation='relu'))

monmodele.add(Dense(num_classes, activation='softmax'))

monmodele.summary()

# initiate RMSprop optimizer
opt = keras.optimizers.RMSprop(learning_rate=0.001)

# Let's train the model using RMSprop
monmodele.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])

monmodele.fit(x=x_train, y=y_train, epochs = epochs, verbose=2, validation_data=(x_test, y_test), shuffle=True)

score = monmodele.evaluate(x_controle,y_controle,verbose=1)
score

predictions = monmodele.predict(x_controle)
predictions.shape

predictions[500,]

consoresultats=np.argmax(y_controle,axis=1)

score

from sklearn.metrics import confusion_matrix
confmat=confusion_matrix(consoresultats, np.argmax(monmodele.predict(x_controle),axis=1))

zed=np.ones((10,10))
for i in range(10):
    zed[i,i]=0
zed
confsansdiag = confmat*zed
confsansdiag

sum(sum(confsansdiag))

import matplotlib.pyplot as plt
plt.imshow(confmat, cmap ='gray')

plt.imshow(confsansdiag, cmap ='gray')
