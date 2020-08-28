import sys
import data_cleaner
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import neighbors
from sklearn.metrics import accuracy_score

#############################################

if __name__ == '__main__':

    if(sys.argv.__len__() > 1):
        dataset = sys.argv[1]
    if(sys.argv.__len__() > 2):
        target_index = sys.argv[2] # 1 for breast cancer data
    
    cleaned = data_cleaner.clean_data(dataset, target_index)
    features = cleaned[0] # M -> 1, B -> 0
    labels = cleaned[1]

    numpy_features = np.array(features)
    numpy_labels = np.array(labels)
    
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=.5)
 
    classifier = tree.DecisionTreeClassifier()
    classifier = neighbors.KNeighborsClassifier()
    classifier.fit(features_train,labels_train)

    predictions = classifier.predict(features_test)

    print(accuracy_score(labels_test,predictions))