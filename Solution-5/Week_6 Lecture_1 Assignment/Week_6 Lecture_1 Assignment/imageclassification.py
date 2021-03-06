# -*- coding: utf-8 -*-
"""imageclassification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P9vpy6wcqO6BHO-pbazSTodO4EUzdUIv

**From uper Menu choose:**
---
Runtime --> Change runtime type:
---
change Hardare accelerator to (gpu)
"""
from keras.layers import BatchNormalization, Dropout
from keras import Sequential, optimizers, Model
from keras.datasets import mnist
import numpy as np
from keras.layers import Dense, Input
from tensorflow.keras.utils import to_categorical

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(type(train_images))
print(train_images.shape)
print(train_images[251].shape)

"""#process the data
#1. convert each image of shape 28*28 to 784 dimensional which will be fed to the network as a single feature
"""

dimData = np.prod(train_images.shape[1:])
print(dimData)
train_data = train_images.reshape(train_images.shape[0], dimData)
test_data = test_images.reshape(test_images.shape[0], dimData)
print(train_data.shape)

"""#convert data to float and scale values between 0 and 1"""

train_data = train_data.astype('float')
test_data = test_data.astype('float')

"""#scale data"""

train_data /= 255.0
test_data /= 255.0

"""change the labels from integer to one-hot encoding. to_categorical is doing the same thing as LabelEncoder()"""

train_labels_one_hot = to_categorical(train_labels)
test_labels_one_hot = to_categorical(test_labels)

print(train_labels_one_hot[0])

"""#creating network"""
# Playing with the Sequential model
# model = Sequential()
#
# model.add(Dense(dimData, activation='tanh', input_shape=(dimData,)))
# model.add(BatchNormalization())
# model.add(Dropout(.2))
#
# model.add(Dense(512, activation='tanh'))
# model.add(BatchNormalization())
# model.add(Dropout(.2))
#
# model.add(Dense(254, activation='tanh'))
#
# model.add(Dense(10, activation='softmax'))
#
# model.summary()

# Functional API representation of Sequential model
inputs = Input(shape=(dimData,))
x = Dense(dimData, activation='tanh')(inputs)
x = BatchNormalization()(x)
x = Dropout(.2)(x)
x = Dense(512, activation='tanh')(x)
x = BatchNormalization()(x)
x = Dropout(.2)(x)
x = Dense(254, activation='tanh')(x)
outputs = Dense(10, activation='softmax')(x)
model = Model(inputs=inputs, outputs=outputs)

"""# Compile model"""

model.compile(optimizer=optimizers.Adam(learning_rate=.0003), loss='categorical_crossentropy', metrics=['accuracy'])

"""# Fit model"""

history = model.fit(train_data, train_labels_one_hot, batch_size=256, epochs=15, verbose=1,
                    validation_data=(test_data, test_labels_one_hot))


# Plot results
import matplotlib.pyplot as plt

plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='val loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()

plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='test accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='lower right')
plt.show()

# plt.imshow(test_data[0].reshape([28,28])) # test_images.reshape(test_images.shape[0],dimData)
plt.imshow(test_images[1010])
plt.show()

res = model.predict(test_data[1010:1011])

# print(res)
print(res.argmax())  # Returns the indices of the maximum values along an axis.
