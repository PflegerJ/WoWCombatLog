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
    #print(parse_rank)
    print(data[0])
    data_without_parse = data[:,:-1]
    data = center(data_without_parse)
    data_cov = np.cov(data_without_parse.T)
    eigenValues, eigenVector = la.eig(data_cov)
    eigenValuesNP, eigenVectorsNP = linalg.eig(data_cov)
    eigen_np = np.array(eigenValues, dtype=float)

    idx = eigenValuesNP.argsort()[::-1] 
    eigenValuesNP = eigenValuesNP[idx]
    eigenVectorsNP = eigenVectorsNP[:,idx]

    axis_names_file = open('data_attributes.txt', 'r')
    axis_names = axis_names_file.readlines()


    print (axis_names[idx[0]], " ", axis_names[idx[1]], " ", axis_names[idx[2]] )
    X = np.matmul(data, eigenVectorsNP[:,:3])

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    #classes = np.arange(499)
    classes = parse_rank
    parse_rank_color = []
    for value in parse_rank:
        if value == 100:
            parse_rank_color.append('yellow')
        elif  value > 95:
            parse_rank_color.append('orange')
        elif  value > 90:
            parse_rank_color.append('purple')


    ax.set_xlabel(axis_names[idx[0]])
    ax.set_ylabel(axis_names[idx[1]])
    ax.set_zlabel(axis_names[idx[2]])
    p = ax.scatter(X[:,0], X[:,1], X[:,2], c=parse_rank_color,)
    fig.colorbar(p)

    plt.show()
    return
