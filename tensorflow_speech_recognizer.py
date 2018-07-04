import tflearn
import speech_data

# Defining hyperparameters

learning_rate = 0.0001

# defining no. of steps we want to train for
training_iters = 300000

#fetching data and applying train_test_split

batch = word_batch = speech_data.mfcc_batch_generator(64)
X,Y = next(batch)
trainX , trainY = X,Y
testX, testY ,X,Y

# creating a neural network
# we use recurrent neural network as we have a sequence of data (i.e spoken words are a sequence of sound waves)

# defining shape of input data i.e a Tensor
net = tflearn.input_data([None,20 ,80])
net = tflearn.lstm(net, 128, dropout=0.8)
net = tflearn.fully_connected(net, 10, activation='softmax')
net = tflearn.regression(net, optimizer='adam', learning_rate=learning_rate, loss='categorical_crossentropy')

model =tflearn.DNN(net, tensorboard_verbose=0)
while 1:
    model.fit(trainX, trainY, n_epochs=10, validation_set =(testX, testY), show_metric=True, batch_size=64)
    _y= model.predict(X)
model.save('tflearn.lstm.model')

print(_y)
print(y)
