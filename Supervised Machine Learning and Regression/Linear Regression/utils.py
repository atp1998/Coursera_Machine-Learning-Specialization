import numpy as np

def load_data():
    data = np.loadtxt("/Users/aungthuphyo/Downloads/Machine Learning Specialization/Week2/ex1data1.txt", delimiter=',')
    X = data[:,0]
    y = data[:,1]
    return X, y

def load_data_multi():
    data = np.loadtxt("/Users/aungthuphyo/Downloads/Machine Learning Specialization/Week2/ex1data2.txt", delimiter=',')
    X = data[:,:2]
    y = data[:,2]
    return X, y

print("everything is loaded")