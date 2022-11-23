import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import h5py
import scipy
from scipy import ndimage
from scipy.special import expit
from PIL import Image


# Generate the data points.
# return X: array containing one data point per column : shape (2,m)
def generate_points(m=100, seed=42):
    rng = np.random.RandomState(seed)
    X = np.zeros((2, m))
    for i in range(m):
        X[0][i] = random.randint(-1, 1)
        X[1][i] = random.randint(-1, 1)
    return X


# Generate random decision boundary
# return w: weight vector representing decision boundary, of shape (3,1)
def random_boundary(seed=42):
    rng = np.random.RandomState(seed)

    # generate two random points A and B
    A = (random.randint(-1, 1), random.randint(-1, 1))
    B = (random.randint(-1, 1), random.randint(-1, 1))
    while (B[0] - A[0]) == 0:
        A = (random.randint(-1, 1), random.randint(-1, 1))
        B = (random.randint(-1, 1), random.randint(-1, 1))

    # calculate vector w
    m = (B[1] - A[1]) / (B[0] - A[0])
    b = -m * A[0] + A[1]
    w = np.array([b, -m, 1], int)
    w = np.reshape(w, (3, 1))
    return w


# Define function that calculates predictions
# input w : weight vector chracterising perceptron model : of shape (3,1)
# input X_ext : data matrix X, extended by a row of ones : of shape (3,m)
# return predictions : sign(w.transpose * x) : of shape (1,m)
def predict(w, X_ext):
    # predictions = np.zeros((1, m))
    # for i in range(m):
    #     predictions[0][i] = w[0] + (w[1] * X_ext[1][i]) + (w[2] * X_ext[2][i])
    # np.sign(predictions, out=predictions)
    predictions = np.sign(np.matmul(w.transpose(), X_ext))
    predictions = np.reshape(predictions, (1, X_ext.shape[1]))
    # print(predictions)
    return predictions


m = 100

# Generate m random data points. X has shape (2,m)
X = generate_points(m)
# add a row of ones. X_ext has shape (3,m)
X_ext = np.vstack((np.ones((1, X.shape[1])), X))

# Generate random boundary. w has shape (3,1)
w = random_boundary()

# Generate labels. Y has shape (1,m)
Y = predict(w, X_ext)


# Visualize the data and the decision boundary
fig, ax = plt.subplots()
ax.scatter(X[0, :], X[1, :], marker="o", c=Y, s=25, edgecolor="k")

# the decision boundary chracterized by vector w
xp = np.array((-1, 1))
yp = -(w[1] / w[2]) * xp - (w[0] / w[2])

plt.axis([-1.1, 1.1, -1.1, 1.1])
plt.plot(xp, yp, "r-")  # decision boundary
plt.show()

# Example of a point
index = 3
print("Point #" + str(index) + " is " + str(X[:, index]))
print("Class #" + str(index) + " is " + str(Y[0, index]))

# Define function for weight update

# input w : current weight vector with shape (3,1)
# input x : misclassified data point (should have shape (3,1))
# input y : label of data point x (scalar)

# return new_w : updated weight vector
def weight_update(w, x, y, learning_rate):
    # print(w)
    # print(x)
    # print(y)

    # --> replace with your code
    new_w = w + (y * x)
    new_w = np.reshape(new_w, (3, 1))
    return new_w


# Initialize weight vector w_ with 0.
# --> replace with your code
w_ = np.zeros((3, 1))
w_ = np.reshape(w, (3, 1))
learning_rate = 0.1
num_iterations = 10

# initialize array to save number of misclassified points in each iteration
num_misses = np.zeros(num_iterations)

for i in range(num_iterations):
    # calculate predictions for all points
    predictions = predict(w_, X_ext)

    # identify indices of misclassified points
    misclassified = []
    for i in range(len(predictions[0])):
        if predictions[0][i] != X_ext[0][i]:
            misclassified.append(i)
    # print(predictions)
    # print(X_ext)
    # print(misclassified)

    # calculate and save number of misclassified points
    # break if there are none
    misclassified_count = len(misclassified)
    if misclassified_count == 0:
        print("done")
        break

    # select random misclassified index
    index = random.randint(0, misclassified_count)

    # perform one weight update using datapoint at selected index
    x = np.array([[X_ext[0][index]], [X_ext[1][index]], [X_ext[2][index]]])
    w_ = weight_update(w_, x, x[0], learning_rate)
    continue
