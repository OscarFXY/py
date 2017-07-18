from Preprocess import get_detaset_XY
import joblib
from sklearn.neighbors.nearest_centroid import NearestCentroid


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
print validX[0], validY[0]
print len(trainX), len(trainY), len(testX), len(testY), len(validX), len(validY)


def build_model():
    clf = NearestCentroid()
    clf.fit(validX, validY)
    joblib.dump(clf, 'D:\Python\models\Nearest.model')
    predictY = clf.predict(validX)
    acc = get_acc(predictY, validY)
    print acc
    return 0


def main():
    build_model()
    return 0


if __name__ == '__main__':
    main()
