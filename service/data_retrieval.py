import csv

def retrieve_data():
    with open('service/cancer-data.csv', 'r') as infile:
        csvreader = csv.reader(infile)
        next(csvreader)
        data = [row for row in csvreader]
        cleaned_data = clean_data(data)
        x = cleaned_data[0]
        y = cleaned_data[1]
    return[x, y]

def clean_data(data):
    uncleaned_len = len(data[1])
    count = 0
    ret = data
    y_array = []
    for i in range(len(data)):
        for j in range(uncleaned_len):
            if ret[i][j] == 'M': 
                ret[i][j] = 1
                y_array.append(1)
            elif ret[i][j] == 'B':
                count = count + 1
                y_array.append(0)
            else:
                ret[i][j] = float(ret[i][j]);
        # ret[i].pop(0)
        # ret[i].pop(0)
        del ret[i][0:2]
        del ret[i][10:]
    print([ret[0]])
    return [ret, y_array]