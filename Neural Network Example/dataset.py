import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
#from auxiliar import transform_data


def get_dataset(random_state=124):

    data_x, data_y = datasets.make_moons(n_samples=2500, shuffle=True, noise=0.20, random_state=random_state)

    X_full_train, X_test, y_full_train, y_test = train_test_split(data_x, data_y, train_size=0.80, random_state=random_state)
    X_train, X_val, y_train, y_val = train_test_split(X_full_train, y_full_train, train_size=0.75, random_state=random_state)
    
    print(f'X_train shape = {X_train.shape}')
    print(f'X_test shape = {X_test.shape}')
    print(f'y_train shape = {y_train.shape}')
    print(f'y_test shape = {y_test.shape}')
    
    X = X_train.T
    Y = y_train.reshape(-1, 1).T
    X_val = X_val.T
    Y_val = y_val.reshape(-1, 1).T
    X_test = X_test.T
    Y_test = y_test.reshape(-1, 1).T
                                                        
    #y_train = y_train.reshape(-1, 1)
    #y_test = y_test.reshape(-1, 1)

    print('X train max value: {:.2f}'.format(X.max()))
    print('X train min value: {:.2f}'.format(X.min()))
   
    

    #print('X = {}'.format(X.flatten()))
    #print('Y = {}'.format(Y.flatten()))

    check_color = np.vectorize((lambda y: 'tab:blue' if (y == 1) else 'tab:orange'))
    color = (check_color(Y).flatten()).tolist()

    plt.scatter(X.T[:, 0], X.T[:, 1], c=color)
    plt.grid('on')
    plt.show()

    return X, Y, X_val, Y_val, X_test, Y_test
