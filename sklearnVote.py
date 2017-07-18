import joblib
from Preprocess import get_detaset_XY
from sklearnBayes import get_acc

print 'load h5file data...'
trainX, trainY, testX, testY, validX, validY = get_detaset_XY()


def load(model_path):
    model = joblib.load(model_path)
    return model


def voteIt():
    final_result = []

    dt = load('C:\Users\Oscar\Python\models\Decision0.614.model')
    gnb = load('C:\Users\Oscar\Python\models\Bayes0.649.model')
    mlp = load('C:\Users\Oscar\Python\models\MLT0.699.model')
    nearest = load('C:\Users\Oscar\Python\models\Nearest0.679.model')
    sgd = load('C:\Users\Oscar\Python\models\sklearnModel0.675.model')
    print 'model start predict...'
    pre_dt = dt.predict(testX)
    pre_gnb = gnb.predict(testX)
    pre_mlp = mlp.predict(testX)
    pre_nearest = nearest.predict(testX)
    pre_sgd = sgd.predict(testX)
    print 'vote box start...'
    for pre_dt_item, pre_gnb_item, pre_mlp_item, pre_nearest_item, pre_sgd_item in zip(pre_dt, pre_gnb, pre_mlp,
                                                                                       pre_nearest, pre_sgd):
        voteBox = []
        voteBox.append(pre_dt_item)
        voteBox.append(pre_gnb_item)
        voteBox.append(pre_mlp_item)
        voteBox.append(pre_nearest_item)
        voteBox.append(pre_sgd_item)
        # print voteBox
        if voteBox.count('sing') > voteBox.count('nosing'):
            final_result.append('sing')
        else:
            final_result.append('nosing')

    return final_result


def modify_error(pre_list):
    modified_list = []
    step = 20
    for list_item in range(0, len(pre_list), step):
        if pre_list[list_item:list_item + step].count('sing') > (step / 2):
            modified_list.extend(step * ['sing'])
        else:
            modified_list.extend(step * ['nosing'])

    return modified_list


def main():
    final_result = voteIt()
    print 'vote acc:', get_acc(final_result, testY)
    modified_list = modify_error(final_result)
    print 'modified acc:', get_acc(modified_list, testY)

    return 0


if __name__ == '__main__':
    main()
