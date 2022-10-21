import csv
import numpy as np
from numpy.lib.nanfunctions import nanquantile
import scipy.linalg as la
import math


def isNaN(num):
    return num != num

def normalize_value(oldMin, oldMax, value):
    numerator = value - oldMin
    denominator = oldMax - oldMin
    return numerator / denominator

def normalize(data):
    for col in range(data.shape[1]):
        col_min = np.min(data[:, col])
        col_max = np.max(data[:, col])
        for row in range(data.shape[0]):
            temp = normalize_value(col_min, col_max, data[row][col])
            if not isNaN(temp):
                data[row][col] = temp
            else:
                data[row][col] = 0
    return data

def euclidean_distance(pointA, pointB):
    sum = 0
    for i in range(len(pointA)):
        sum = sum + (pointA[i] + pointB[i]) ** 2
    return sum ** 0.5




test_file = open('sf_raw_data.csv')

csvreader = csv.reader(test_file)
data = []
line = next(csvreader)
data_point_count = 0

data.extend(line)
data_point_count += 1
  
i = 1
for row in csvreader:
    if row != []:
        print(len(row))
        if len(row) == 82:
            data.extend(row)
            data_point_count += 1


data_numpy = np.array(data).astype(np.float)
data_numpy = np.reshape(data_numpy, (data_point_count, 82))



a =2


data_numpy = normalize(data_numpy)




mean = data_numpy.mean(axis=0)

a =2
for i in range(data_point_count):
    a = data_numpy[i]
    data_numpy[i] = data_numpy[i] - mean[i]


c = np.transpose(data_numpy)

cov = np.cov(c)

eigenValues, eigenVector = la.eig(cov)
a= 2
b = 2