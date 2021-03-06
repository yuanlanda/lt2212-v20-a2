import argparse
import random
import string
from sklearn.datasets import fetch_20newsgroups
from sklearn.base import is_classifier
from sklearn.decomposition import PCA
from sklearn.decomposition import TruncatedSVD
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score,accuracy_score,recall_score,f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
import numpy as np
random.seed(42)


###### PART 1
#DONT CHANGE THIS FUNCTION
def part1(samples):
    #extract features
    X = extract_features(samples)
    assert type(X) == np.ndarray
    print("Example sample feature vec: ", X[0])
    print("Data shape: ", X.shape)
    return X


def extract_features(samples):
    print("Extracting features ...")

    samples_words_list = []
    words_index_dict_tmp = {}
    words_index_dict = {}
    for sample in samples:
        words_tmp = sample.lower().split()

        # filter numbers and punctuation
        words = [word for word in words_tmp if word.isalpha()]

        samples_words_list.append(words)

        # create unique word index dict
        i = 0
        for word in words:
            if word not in words_index_dict_tmp:
                words_index_dict_tmp[word] = i
                i += 1

    # Filter the word occurs less than 5 counts in the whole corpus
    # The ndarray columns is sorted by the keys of this dict
    j = 0
    for key in words_index_dict_tmp.keys():
        if words_index_dict_tmp[key] > 5:
            words_index_dict[key] = j
            j += 1
    
    unique_word_list = tuple(words_index_dict.keys())

    # create feature ndarray, rows represent samples, columns represent words
    features = np.zeros((len(samples), len(unique_word_list)))

    sample_index = 0  
    for sample_words in samples_words_list:
        sample_list = np.zeros(len(unique_word_list))

        for sample_word in sample_words:
            if sample_word in words_index_dict.keys():
                index = words_index_dict[sample_word]
                sample_list[index] += 1

        features[sample_index] = sample_list
        sample_index += 1
    
    return features


##### PART 2
#DONT CHANGE THIS FUNCTION
def part2(X, n_dim):
    #Reduce Dimension
    print("Reducing dimensions ... ")
    X_dr = reduce_dim(X, n=n_dim)
    assert X_dr.shape != X.shape
    assert X_dr.shape[1] == n_dim
    print("Example sample dim. reduced feature vec: ", X[0])
    print("Dim reduced data shape: ", X_dr.shape)
    return X_dr


def reduce_dim(X,n=10):
    svd = TruncatedSVD(n_components=n)
    return svd.fit_transform(X)


##### PART 3
#DONT CHANGE THIS FUNCTION EXCEPT WHERE INSTRUCTED
def get_classifier(clf_id):
    if clf_id == 1:
        clf = GaussianNB()
    elif clf_id == 2:
        clf = DecisionTreeClassifier()
    else:
        raise KeyError("No clf with id {}".format(clf_id))

    assert is_classifier(clf)
    print("Getting clf {} ...".format(clf.__class__.__name__))
    return clf

#DONT CHANGE THIS FUNCTION
def part3(X, y, clf_id):
    #PART 3
    X_train, X_test, y_train, y_test = shuffle_split(X,y)

    #get the model
    clf = get_classifier(clf_id)

    #printing some stats
    print()
    print("Train example: ", X_train[0])
    print("Test example: ", X_test[0])
    print("Train label example: ",y_train[0])
    print("Test label example: ",y_test[0])
    print()


    #train model
    print("Training classifier ...")
    train_classifer(clf, X_train, y_train)


    # evalute model
    print("Evaluating classcifier ...")
    evalute_classifier(clf, X_test, y_test)


def shuffle_split(X,y):
    return train_test_split(X, y, test_size=0.2)


def train_classifer(clf, X, y):
    assert is_classifier(clf)
    clf.fit(X, y)


def evalute_classifier(clf, X, y):
    assert is_classifier(clf)
    y_pred = clf.predict(X)
    print("Accuracy:", accuracy_score(y, y_pred))
    print("Precision:", precision_score(y, y_pred, average='weighted'))
    print("Recall:", recall_score(y, y_pred, average='weighted'))
    print("F-measure:", f1_score(y, y_pred,average='weighted'))

######
#DONT CHANGE THIS FUNCTION
def load_data():
    print("------------Loading Data-----------")
    data = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)
    print("Example data sample:\n\n", data.data[0])
    print("Example label id: ", data.target[0])
    print("Example label name: ", data.target_names[data.target[0]])
    print("Number of possible labels: ", len(data.target_names))
    return data.data, data.target, data.target_names


#DONT CHANGE THIS FUNCTION
def main(model_id=None, n_dim=False):

    # load data
    samples, labels, label_names = load_data()


    #PART 1
    print("\n------------PART 1-----------")
    X = part1(samples)

    #part 2
    if n_dim:
        print("\n------------PART 2-----------")
        X = part2(X, n_dim)

    #part 3
    if model_id:
        print("\n------------PART 3-----------")
        part3(X, labels, model_id)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n_dim",
                        "--number_dim_reduce",
                        default=False,
                        type=int,
                        required=False,
                        help="int for number of dimension you want to reduce the features for")

    parser.add_argument("-m",
                        "--model_id",
                        default=False,
                        type=int,
                        required=False,
                        help="id of the classifier you want to use")

    args = parser.parse_args()
    main(   
            model_id=args.model_id, 
            n_dim=args.number_dim_reduce
            )
