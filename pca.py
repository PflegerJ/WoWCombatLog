import numpy as np
import csv
import numpy.linalg as linalg
import scipy.linalg as la
import matplotlib.pyplot as plt
import matplotlib.cm as cm

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
        if line != []:
            data_points = len(line)
            data_entities += 1
            data.extend(line)
    
    print(data_points)
    np_data = np.array(data, dtype=float)
    np_data = np.reshape(np_data, (data_entities, data_points))
    return np_data

def pca(fileName):
    data = readDataCSV(fileName)
    parse_rank = data[:,[-1]]
    print(parse_rank)
    data = center(data)
    data_cov = np.cov(data.T)
    eigenValues, eigenVector = la.eig(data_cov)
    eigenValuesNP, eigenVectorsNP = linalg.eig(data_cov)
    eigen_np = np.array(eigenValues, dtype=float)

    idx = eigenValuesNP.argsort()[::-1] 
    eigenValuesNP = eigenValuesNP[idx]
    eigenVectorsNP = eigenVectorsNP[:,idx]


    X = np.matmul(data, eigenVectorsNP[:,:3])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    classes = parse_rank
    p = ax.scatter(X[:,0], X[:,1], X[:,2], c=classes,)
    fig.colorbar(p)

    plt.show()
    return
