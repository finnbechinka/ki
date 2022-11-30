import numpy as np  # Scientific computing
import matplotlib.pyplot as plt  # plot graphs
import matplotlib.lines as mlines
import sklearn.datasets
import h5py  # work with dataset stored in H5 files
import scipy  # use your own pictures
from PIL import Image  # use your own pictures
from scipy import ndimage
from scipy.special import expit  # expit is the sigmoid function

# Generating random dataset with sklearn

np.random.seed(7)
X1_raw, Y1_raw = sklearn.datasets.make_classification(
    n_samples=100, n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1
)

# Visualize the data:
fig, ax = plt.subplots()
ax.scatter(X1_raw[:, 0], X1_raw[:, 1], marker="o", c=Y1_raw, s=25, edgecolor="k")
plt.show()

# Check shapes
print(X1_raw.shape)
print(Y1_raw.shape)

# Example of a point
# index = 1
# print("Point #" + str(index) + " : " + str(X1_raw[index,:]))
# print("Class #" + str(index) + " : " + str(Y1_raw[index]))

# We need one Datapoint per column
# X1_raw has shape (100,2), one row per instance
# transpose to (2, 100), one column per instance
X1 = np.transpose(X1_raw)

# reshape Y1 from (100,) to (1, 100)
Y1 = Y1_raw.reshape(1, Y1_raw.shape[0])

# check shapes
print(X1.shape)
print(Y1.shape)

### Q : What is the difference between the shapes (100,) and (1,100) ?

# Extend every input by x_0 = 1 and check shape
X = np.vstack((np.ones((1, 100)), X1))
Y = Y1
print(X.shape)
print(Y.shape)

# LogisticRegression() method from sklearn
# --> You can use this result as a baseline and compare your own result against it.

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression(solver="lbfgs", random_state=42)
log_reg.fit(X1_raw, Y1_raw)

# Note: "lbfgs" is not gradient descent. The call of the fit() function runs a
# different optimization algorithm to calculate the optimum solution.
# See: http://users.iems.northwestern.edu/~nocedal/lbfgsb.html

# predicted probabilities of the model for all datapoints
y_proba = log_reg.predict_proba(X1_raw)
# predicted classes of the model for all datapoints
y_pred = log_reg.predict(X1_raw)

# compare predicted probabilities and classes to the ground truth (true labels)
# for the first five datapoints
print(y_proba[0:5])
print(y_pred[0:5])
print(Y1_raw[0:5])

# Q: the model classifies the 4th and 5th points both as "1";
# in which case the model is more sure about its prediction?

# the calculated "best" weights/parameters
w0 = log_reg.intercept_[0]
w1 = log_reg.coef_.T[0][0]
w2 = log_reg.coef_.T[1][0]
print("w0: " + str(w0))
print("w1: " + str(w1))
print("w2: " + str(w2))

# the decision boundary (determine two points on the line)
xp = np.array((-2, 2.6))
yp = -(w0 + w1 * xp) / w2

# plot decision boundaries
# Visualize the data:
colors = ["y", "r", "g", "b", "c", "m"]
fig, ax = plt.subplots()
ax.scatter(X1_raw[:, 0], X1_raw[:, 1], marker="o", c=Y1_raw, s=25, edgecolor="k")
plt.axis([-2, 2.5, -2.5, 2.5])
plt.plot(xp, yp, "r-")
plt.show()

# how good does the model fit the training data?
# training accuracy: what fraction of the training data is classified correctly?

acc = 1 - np.mean(np.abs(Y1_raw - y_pred))
print("training accuracy: " + str(acc))


def init_parameters(n):
    np.random.seed(2)
    # -- start of your code
    A = np.random.uniform(-1, 1, 2)
    B = np.random.uniform(-1, 1, 2)

    m = (B[1] - A[1]) / (B[0] - A[0])
    b = A[1] - (m * A[0])

    w = np.array([b, -m, 1]).reshape((n + 1, 1))
    # -- end of your code

    assert w.shape == (n + 1, 1)
    return w


def forward_pass(X, w):
    # Hint: use scipy.special.expit as sigmoid function
    # -- start of your code
    z = np.dot(np.transpose(w), X)
    A = expit(z)
    # -- end of your code

    assert A.shape == (1, X.shape[1])
    return A


def calculate_loss(A, Y):

    # -- start of your code
    L = -Y * np.log(A) - (1 - Y) * np.log(1 - A)
    # -- end of your code

    assert L.shape == Y.shape
    return L


def calculate_cost(loss):

    # -- start of your code
    m = X.shape[1]
    cost = (np.sum(loss)) / m
    # -- end of your code

    assert isinstance(cost, float) or isinstance(cost, int)
    cost = np.squeeze(cost)
    assert cost.shape == ()

    return cost


def calculate_gradients(X, Y, A):

    # -- start of your code
    m = X.shape[1]
    dw = (1 / m) * np.dot(X, np.transpose((A - Y)))
    # -- end of your code

    assert dw.shape == (X.shape[0], 1)
    return dw


def update_parameters(w, dw, learning_rate=0.01):

    # -- start of your code
    w_new = w - learning_rate * dw
    # -- end of your code

    assert w_new.shape == w.shape
    return w_new


# dataset stored in X and Y
n = X.shape[0] - 1  # number of features
m = X.shape[1]  # number of examples/datapoints

# init
w = init_parameters(n)
print(w)

# forward pass
A = forward_pass(X, w)
print(A)

# loss
loss = calculate_loss(A, Y)
print(loss)

# cost
cost = calculate_cost(loss)
print(cost)

# calculate gradients
dw = calculate_gradients(X, Y, A)
print("dw = " + str(dw))

# update parameters

# Note: The size of the step is controlled by the learning_rate
learning_rate = 0.001

print("Parameters and Cost Before Update")
print("w = " + str(w))
print("Cost = " + str(cost))

w = update_parameters(w, dw, learning_rate)

print("\nParameters and Cost After Update")
print("w = " + str(w))

A = forward_pass(X, w)
loss = calculate_loss(A, Y)
cost = calculate_cost(loss)
print("Cost = " + str(cost))

# dataset
n = X.shape[0] - 1  # number of features
m = X.shape[1]  # number of examples/datapoints

# init parameters, set hyperparameters
w = init_parameters(n)
learning_rate = 0.01
num_iterations = 2000
costs = []

for i in range(num_iterations):
    # -- start of your code
    A = forward_pass(X, w)
    loss = calculate_loss(A, Y)
    cost = calculate_cost(loss)

    if i % 100 == 0:
        costs.append(cost)

    dw = calculate_gradients(X, Y, A)
    w = update_parameters(w, dw, learning_rate)
    # -- end of your code

    if cost and i % 100 == 0:
        print("Cost after iteration %i: %f" % (i, cost))

# Plot learning curve (with costs)
costs = np.squeeze(costs)
plt.plot(costs)
plt.ylabel("cost")
plt.xlabel("iterations (per hundreds)")
plt.title("Learning rate =" + str(learning_rate))
plt.show()

# Evaluate your model - how many points are classified correctly?

# -- start of your code

accuracy = None

# -- end of your code

print("Train accuracy: {} %".format(accuracy))
