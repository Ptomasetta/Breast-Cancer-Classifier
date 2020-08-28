import sys
import data_cleaner
import numpy as np

#############################################

if __name__ == '__main__':

    if(sys.argv.__len__() > 1):
        dataset = sys.argv[1]
    if(sys.argv.__len__() > 2):
        target_index = sys.argv[2] # 1 for breast cancer data
    
    cleaned = data_cleaner.clean_data(dataset, target_index)
    features = cleaned[0] # M -> 1, B -> 0
    labels = cleaned[1]
    print(len(cleaned[0]))
    print(len(cleaned[1]))
    numpy_features = np.array(features)
    numpy_labels = np.array(labels)
    print(cleaned[0])

    
    