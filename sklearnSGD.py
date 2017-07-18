from Preprocess import get_detaset_XY
import joblib
from sklearn.linear_model import SGDClassifier


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


def correct_predict_model(predict):
    modified_list = []
    step = 5
    for lsit_item in range(0, len(predict), step):
        if list(predict[lsit_item:lsit_item + step]).count('sing') > (step / 2):
            modified_list.extend(step * ['sing'])
        else:
            modified_list.extend(step * ['nosing'])
    return modified_list


def build_model():
    clf = SGDClassifier(loss="hinge", penalty="l2", n_iter=20)
    clf.fit(validX, validY)
    joblib.dump(clf, 'D:\Python\models\sklearnSGD.model')
    predictY = clf.predict(validX)
    predictY = correct_predict_model(predictY)

    acc = get_acc(predictY, validY)

    print acc,
    return acc


def main():
    build_model()
    return 0


if __name__ == '__main__':
    main()
