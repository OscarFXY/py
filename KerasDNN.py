import numpy
from keras.callbacks import EarlyStopping
from Preprocess import get_detaset_XY
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from sklearnBayes import get_acc

trainX, trainY, testX, testY, validX, validY = get_detaset_XY('D:\DATA\dataset.h5')
# fix random seed for reproducibility
seed = 1007
numpy.random.seed(seed)
# encode class values as integers
encoder = LabelEncoder()
encoder.fit(trainY)
trainY = encoder.transform(trainY)
testY = encoder.transform(testY)
validY = encoder.transform(validY)


# baseline model
def create_baseline():
    # create model
    model = Sequential()
    model.add(Dense(60, input_dim=12, init='normal', activation='relu'))
    model.add(Dense(1, init='normal', activation='sigmoid'))
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# evaluate baseline model with standardized dataset
def main():
    model = create_baseline()
    callbacks = [EarlyStopping(monitor='val_loss', patience=2, verbose=0)]
    model.fit(trainX, trainY, batch_size=100, nb_epoch=200, validation_data=(validX, validY), callbacks=callbacks)
    pre_testY = model.predict_classes(testX)
    print '\n acc: ',get_acc(pre_testY,testY)

    return 0


if __name__ == '__main__':
    main()
