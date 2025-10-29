import numpy as np

def load_house_data():
    data = np.loadtxt("/Users/aungthuphyo/Downloads/Machine Learning Specialization/Week2/houses.txt", delimiter=',', skiprows=1)
    X = data[:,:4]
    y = data[:,4]
    return X, y