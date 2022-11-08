import numpy as np
import csv
import numpy.linalg as linalg
import scipy.linalg as la
import matplotlib.pyplot as plt

#center data around 0
def center(data):
    for i in range( data.shape[1]):

        mean = np.mean(data[:,i])
        #print (mean)
        data[:,i] = data[:,i] - mean
    
    return data

def readDataCSV(fileName):
    file = open(fileName)
    csvreader = csv.reader(file)
    data = []
    data_points = 0
    data_entities = 0
    for line in csvreader:
        #print(line)
        if line != []:
            data_points = len(line)
            data_entities += 1
            data.extend(line)
    
    print(data_points)
   # print(data_points)
    np_data = np.array(data, dtype=float)
    np_data = np.reshape(np_data, (data_entities, data_points))
    #print(np_data.shape[0])
    return np_data


test_data = [0, .4, .7, 1, 0, .2, .8, 1, 0, .8, .9, 1]
test_data = np.array(test_data)
test_data = np.reshape(test_data, (3, 4))
#print(test_data)
data = readDataCSV('data1Normal.csv')
#data = data[~np.isnan(data)]
#print(data.shape)
#print(data)
#print(data.shape[0])
data = center(data)

#print(data[:,0])
# calculate the covariance matrix
data_cov = np.cov(data.T)
#print(data_cov)
#print(data_cov)
# calculate the unite eigenvectors and values
eigenValues, eigenVector = la.eig(data_cov)
eigenValuesNP, eigenVectorsNP = linalg.eig(data_cov)
eigen_np = np.array(eigenValues, dtype=float)
max_e = max(eigenValues)
print(eigenValues)
print(eigenValuesNP)
print(max_e)
max_eNP = max(eigenValuesNP)
print(max_eNP)
#print (eigen_np)


idx = eigenValuesNP.argsort()[::-1]   
eigenValuesNP = eigenValuesNP[idx]
eigenVectorsNP = eigenVectorsNP[:,idx]

print(eigenValuesNP)
print(idx)
print (np.where(eigenValues == eigenValues[2]))

print(eigenVectorsNP.shape)

X = np.matmul(data, eigenVectorsNP[:,:3])
print("++++++++++++++++++++++++")
print(X[:,0])
print(X[:,1])
print(X[:,2])
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(X[:,0], X[:,1], X[:,2], marker='x')
#plt.scatter(X[:,0], X[:,1])
plt.show()
