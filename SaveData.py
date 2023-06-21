import pickle
import numpy as np

def makeWindow(dim, theta, r):
    window = np.zeros((dim, dim, dim))
    x_cen = dim/2
    y_cen = dim/2
    z_cen = -r/np.tan(theta)
    axis = np.array([0, 0, 1])
    for i in range(dim):
        for j in range(dim):
            for k in range(1, dim):
                test = np.array([i-x_cen, j-y_cen, k-z_cen])
                cosphi = np.dot(test, axis)/np.linalg.norm(test)
                if(cosphi > abs(np.cos(theta))):
                    window[i, j, k] =  1
    fileName = "window_"+ str(dim)
    with open(fileName, 'wb') as outp:
        pickle.dump(window, outp)
    return window

def readFile(path):
    file = open(path, "r")
    x_dat, y_dat, z_dat = np.loadtxt(path, unpack = True)
    with open("data_x", 'wb') as outp1:
        pickle.dump(x_dat, outp1)
    with open("data_y", 'wb') as outp2:
        pickle.dump(y_dat, outp2)
    with open("data_z", 'wb') as outp3:
        pickle.dump(z_dat, outp3)
    return x_dat, y_dat, z_dat