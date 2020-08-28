import csv

def clean_data(dataset, target_index):
    with open('datasets/'+dataset, 'r') as infile:
        csvreader = csv.reader(infile)
        feature_names = next(csvreader)
        data = [row for row in csvreader]
        domains = [list(set(x)) for x in zip(*data)]
        labels_and_features = get_labels_and_features(data)
        labels = labels_and_features[0]
        features = labels_and_features[1]
    return[labels, features]

def get_labels_and_features(data):
    count = 0
    ret = data
    features_array = []
    for i in range(len(data)):
        for j in range(len(data[1])):
            if ret[i][j] == 'M': 
                ret[i][j] = 1
                features_array.append(1)
            elif ret[i][j] == 'B':
                count = count + 1
                features_array.append(0)
            else:
                ret[i][j] = float(ret[i][j]);
        # ret[i].pop(0)
        # ret[i].pop(0)
    return [ret, features_array]