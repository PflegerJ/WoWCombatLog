import numpy as np
import csv

def normalize_point(dataPoint, min, max, new_min = 0, new_max = 1):
    top = dataPoint - min
    bottom = max - min
    ratio = top / bottom
    normalized_data = ratio * (new_max - new_min) + new_min

    return normalized_data

def normalize_data(data, row_size, col_size):
    nan_count = 0
    for i in range(col_size):
        min1 = min(data[:, i])
        max1 = max(data[:, i])
        if (min1 == max1):
            print(i)
            nan_count += 1
        for j in range(row_size):
            data[j, i] = normalize_point(data[j, i], min1, max1)
    
    data = data[~np.isnan(data)]
    data = np.reshape(data, (row_size, col_size - nan_count))
    return data


def writeToFile(fileName, data):
    file = open(fileName, 'w')
    wr = csv.writer(file)
    wr.writerows(data)

    file.close()
    return

def normalize(file_in_name, file_out_name):
    file_in = open(file_in_name)
    csvreader = csv.reader(file_in)
    data = []
    data_entities = 0
    for line in csvreader:
        if line != []:
            data_points = len(line)
            data_entities += 1
            data.extend(line)
    
    np_data = np.array(data, dtype=float)
    np_data = np.reshape(np_data, (data_entities, data_points))
    parse_rank = np_data[:,0:1]
    normalized_data = normalize_data(np_data[:,1:], data_entities, data_points - 1)
    combined = np.append(normalized_data, parse_rank, axis=1)
    writeToFile(file_out_name, combined)
    return

    """
test_file = open('data1Write.csv')
csvreader = csv.reader(test_file)
data = []
#line = next(csvreader)
data_points = 0
data_entities = 0
for line in csvreader:
    print(line)
    if line != []:
        data_points = len(line)
        data_entities += 1
        data.extend(line)


np_data = np.array(data, dtype=float)
np_data = np.reshape(np_data, (data_entities, data_points))



np_data = normalize(np_data, data_entities, data_points)

print(np_data.dtype)
writeToFile('data1Normal2.csv', np_data)


def a(blah):
    return blah + 2
#print(np_data[:,0])
#print(np.mean(np_data[:,0]))
#print(np_data)
#print(np_data.shape)
#print (len(line))

"""