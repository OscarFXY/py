from Preprocess import get_detaset_XY
import joblib
from sklearn.neural_network import MLPClassifier


def get_acc(predictList, trueList):  # accurate
    right = 0
    total = 0
    for pre, tru in zip(predictList, trueList):
        total += 1
        if pre == tru:
            right += 1
    acc = right / 1.0 / total
    return acc


trainX, trainY, testX, testY, validX, validY = get_detaset_XY('D:\DATA\dataset.h5')
print trainX[0], trainY[0]
print len(trainX), len(trainY), len(testX), len(testY), len(validX), len(validY)


def build_model():
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                        hidden_layer_sizes=(5, 2), random_state=1, max_iter=100)

    clf.fit(trainX, trainY)
    joblib.dump(clf, 'D:\Python\models\MLT.model')
    predictY = clf.predict(testX)
    acc = get_acc(predictY, testY)
    print acc
    return 0


def main():
    build_model()
    return 0


if __name__ == '__main__':
    main()
