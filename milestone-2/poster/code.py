import numpy as np
import h5py
import scipy
import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from PIL import Image
from scipy import ndimage
from scipy.special import expit  # expit is the sigmoid function
import pandas as pd

plt.rcParams["figure.figsize"] = (5.0, 4.0)  # set default size of plots
plt.rcParams["image.interpolation"] = "nearest"
plt.rcParams["image.cmap"] = "gray"


np.random.seed(1)


def sigmoid(Z):
    """
    Implements the sigmoid activation in numpy
    Arguments:
      Z -- numpy array of any shape
    Returns:
      A -- output of sigmoid(z), same shape as Z
    """
    A = 1 / (1 + np.exp(-Z))

    return A


def relu(Z):
    """
    Implement the RELU function.
    Arguments:
      Z -- Output of the linear layer, of any shape
    Returns:
      A -- Post-activation parameter, of the same shape as Z
    """
    A = np.maximum(0, Z)
    assert A.shape == Z.shape

    return A

    # To be used in the backpropagation step


def relu_backward(dA, Z):
    """
    Arguments:
      dA --- gradients for the activations of the current layer l: any shape
      Z --- input of the relu(Z) during the forward propagation step of the current layer l
    Returns:
      dZ --- gradients for Z (Partial derivative of the cost with respect to Z)
    """
    dZ = np.array(dA, copy=True)  # just converting dz to a correct object.
    dZ[Z <= 0] = 0  # When z <= 0, you should set dz to 0.
    assert dZ.shape == Z.shape

    return dZ


def sigmoid_backward(dA, Z):
    """
    Arguments:
      dA --- gradients for the activations of the current layer l: any shape
      Z --- input of the relu(Z) during the forward propagation step of the current layer l
    Returns:
      dZ -- gradients for Z (Partial derivative of the cost with respect to Z)
    """
    s = 1 / (1 + np.exp(-Z))
    dZ = np.multiply(dA, np.multiply(s, (1 - s)))
    assert dZ.shape == Z.shape

    return dZ


def plot_costs(costs, learning_rate):
    plt.plot(np.squeeze(costs))
    plt.ylabel("cost")
    plt.xlabel("iterations (per hundreds)")
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()


dataset = pd.read_csv("./IRIS.csv")
# print(dataset)
Y1_raw_str = dataset["species"].to_numpy()
X1_raw = dataset.drop("species", axis=1).to_numpy()
Y1_raw = np.empty((Y1_raw_str.shape[0], 3))
for i in range(len(Y1_raw_str)):
    if Y1_raw_str[i] == "Iris-setosa":
        Y1_raw[i] = np.array([1, 0, 0])
    if Y1_raw_str[i] == "Iris-versicolor":
        Y1_raw[i] = np.array([0, 1, 0])
    if Y1_raw_str[i] == "Iris-virginica":
        Y1_raw[i] = np.array([0, 0, 1])


# Visualize the data:
# fig, ax = plt.subplots()
# ax.scatter(X1_raw[:, 0], X1_raw[:, 1], marker="o", c=Y1_raw, s=25, edgecolor="k")
# plt.show()

# print(X1_raw.shape)
# print(Y1_raw.shape)

X1 = np.transpose(X1_raw)
Y1 = np.transpose(Y1_raw)
# print(X1.shape)
# print(Y1.shape)
print(X1)
print(Y1)


def init_params(n_prev, n_curr):
    """
    Arguments:
    n_prev --- size of the previous layer (size of the input of the current layer)
    n_curr --- size of the current layer

    Returns:
    parameters --- (W, b): weight matrix W of shape (n_curr, n_prev), bias vector b of shape (n_curr, 1)
    """

    W = np.random.randn(n_curr, n_prev) * 0.01
    b = np.zeros((n_curr, 1))

    return (W, b)


def forward_step(A_prev, W, b, activation):
    """
    Arguments:
    A_prev --- activations of previous layer: numpy array of shape (size of prev layer, number of examples)
    W --- weight matrix: numpy array of shape (size of current layer, size of previous layer)
    b --- bias vector: numpy array of shape (size of current layer, 1)
    activation --- activation of current layer: "sigmoid" or "relu" (as string)

    Returns:
    (Z,A) --- logits and outputs of current layer: each of shape (size of current layer, number of examples)
    """

    # The linear part of a layer's forward propagation.
    Z = np.dot(W, A_prev) + b
    assert Z.shape == (W.shape[0], A_prev.shape[1])

    # The none-linear part
    if activation == "sigmoid":
        A = sigmoid(Z)

    elif activation == "relu":
        A = relu(Z)

    assert A.shape == (W.shape[0], A_prev.shape[1])

    return (Z, A)


def compute_cost(Y_hat, Y):
    """
    Arguments:
    Y_hat --- predictions: vector of shape (1, number of examples)
    Y --- labels: vector of shape (1, number of examples)

    Returns:
    cost --- cross-entropy cost
    """

    m = Y.shape[1]  # number of examples

    sum = np.sum(np.multiply(Y, np.log(Y_hat)) + np.multiply((1 - Y), np.log(1 - Y_hat)))
    cost = (-1 / m) * sum

    cost = np.squeeze(cost)  # turns [[17]] into 17
    assert cost.shape == ()

    return cost


def backward_step(A_prev, W, b, a, Z, dA):
    """
    Arguments:
    dA --- gradients for the activations of current layer l
    cache --- (A_prev, W, b, Z) tuple stored in the forward_step of layer l
    activation --- the activation function used in current layer l: "sigmoid" or "relu"

    Returns:
    dA_prev --- Gradient for the activations of the previous layer l-1: same shape as A_prev
    dW --- gradients for the weights W of current layer l: same shape as W
    db --- gradients for the biases b of current layer l: same shape as b
    """
    m = A_prev.shape[1]

    # The non-linear backward part
    if a == "relu":
        dZ = relu_backward(dA, Z)

    elif a == "sigmoid":
        dZ = sigmoid_backward(dA, Z)

    # The linear backward part
    dW = 1 / m * np.dot(dZ, np.transpose(A_prev))
    db = 1 / m * np.sum(dZ, axis=1, keepdims=True)
    dA_prev = np.dot(np.transpose(W), dZ)

    assert dA_prev.shape == A_prev.shape
    assert dW.shape == W.shape
    assert db.shape == b.shape

    return (dA_prev, dW, db)


def update_parameters(parameters, gradients, learning_rate):
    """
    Arguments:
    parameters --- (W,b,a): parameters of current layer l
    grads --- (dW, db): gradients for the weights and biases of current layer l

    Returns:
    (W_new, b_new) --- updated weights and biases
    """
    (W, b, a) = parameters
    (dW, db) = gradients
    W_new = W - learning_rate * dW
    b_new = b - learning_rate * db

    return (W_new, b_new, a)


def init_model(layer_dims, activations):
    """
    Arguments:
    layer_dims --- array of dimensions, for each layer including input layer (e.g. (2,3,1))
    activations --- array of activation functıons to be used, for each layer except the input layer (e.g. ("relu", "sigmoid"))

    Returns:
    model --- array of (W, b, activation) tuples, one for each layer
    """

    L = len(layer_dims) - 1
    model = [None for i in range(0, L + 1, 1)]
    model[0] = (None, None, None)  # Interpreting Input layer as layer number 0 (no parameters, no activation)

    for l in range(1, L + 1, 1):
        (W, b) = init_params(layer_dims[l - 1], layer_dims[l])
        model[l] = (W, b, activations[l - 1])

    return model


def train_model(model, X, Y, num_iterations=3000, learning_rate=0.01, print_cost=False):
    """

    Arguments:
    model --- model to be trained: array of (W, b, activation) tuples, one for each layer
    X --- input data: of shape (n, number of examples)
    Y --- labels for the input data: of shape (1, number of examples)
    num_iterations --- number of iterations of the optimization loop
    learning_rate --- learning rate of the gradient descent update rule
    print_cost --- If set to True, this will print the cost every 100 iterations

    Returns:
    model --- model with trained parameters
    costs --- costs saved every 100th itertion during training
    """

    n = X.shape[0]  # number of features
    m = X.shape[1]  # number of examples
    L = len(model) - 1  # number of layers in model (input layer not included)
    # print(n)
    # print(model)
    # print(model[1][0].shape[1])
    assert n == model[1][0].shape[1]  # n == (layer 1 -> W -> number of columns) ?

    costs = []  # to keep track of the cost
    grads = [None for i in range(0, L + 1, 1)]
    grads[0] = (None, None)  # no gradients for input layer 0
    outputs = [None for i in range(0, L + 1, 1)]
    outputs[0] = (None, X)  # "Outputs" of input layer are the datapoints X

    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation
        A_prev = X
        for l in range(1, L + 1, 1):
            (W, b, a) = model[l]
            (Z, A) = forward_step(A_prev, W, b, a)
            outputs[l] = (Z, A)
            A_prev = A
        AL = A_prev  # Output of last layer L (i.e. predictions)
        # print(AL)
        # Compute cost
        cost = compute_cost(AL, Y)

        # Initialize backward propagation by calculating gradients for AL
        dAL = -np.divide(Y, AL) + np.divide((1 - Y), (1 - AL))

        # Backward propagation
        dA = dAL
        for l in range(L, 0, -1):
            (W, b, a) = model[l]
            (Z_prev, A_prev) = outputs[l - 1]
            (Z, A) = outputs[l]
            (dA_prev, dW, db) = backward_step(A_prev, W, b, a, Z, dA)
            grads[l] = (dW, db)
            dA = dA_prev

        # Update model parameters
        for l in range(1, L + 1, 1):
            model[l] = update_parameters(model[l], grads[l], learning_rate)

        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print("Cost after iteration {}: {}".format(i, np.squeeze(cost)))
        if i % 100 == 0:
            costs.append(cost)

    return model, costs


def model_forward(model, X):
    """
    Implement forward propagation for the given neural network model

    Arguments:
    model --- trained model
    X --- data: numpy array of shape (input size, number of examples)

    Returns:
    AL --- putput of last layer (predictions)
    outputs --- list of calculated outputs during forward_step
    """

    L = len(model) - 1  # number of layers in the neural network (input layer not included)
    outputs = [None for i in range(0, L + 1, 1)]
    outputs[0] = (None, X)  # "Outputs" of input layer are the datapoints X

    # Forward propagation
    A_prev = X
    for l in range(1, L + 1, 1):
        (W, b, a) = model[l]
        (Z, A) = forward_step(A_prev, W, b, a)
        outputs[l] = (Z, A)
        A_prev = A
    AL = A_prev  # Output of last layer L (i.e. predictions)

    assert AL.shape == (3, X.shape[1])

    return AL, outputs


def model_accuracy(AL, Y):
    """
    Arguments:
    AL --- probability outputs to be assessed
    Y --- ground truth (expected true labels)

    Returns:
    p --- predicted classes for the given dataset X
    accuracy --- accuracy of the predictions (correct rate)
    """
    m = Y.shape[1]  # number of data points
    p = np.empty(AL.shape)
    # convert probas to 0/1 predictions
    for i in range(0, AL.shape[1]):
        x = AL[0, i]
        y = AL[1, i]
        z = AL[2, i]
        if x > y and x > z:
            p[0, i] = 1
            p[1, i] = 0
            p[2, i] = 0
        elif y > x and y > z:
            p[0, i] = 0
            p[1, i] = 1
            p[2, i] = 0
        elif z > x and z > y:
            p[0, i] = 0
            p[1, i] = 0
            p[2, i] = 1

    sum = 0
    for i in range(0, p.shape[1]):
        x1 = p[0, i]
        y1 = p[1, i]
        z1 = p[2, i]
        x2 = Y[0, i]
        y2 = Y[1, i]
        z2 = Y[2, i]
        if x1 == x2 and y1 == y2 and z1 == z2:
            sum += 1

    accuracy = sum / m

    return (p, accuracy)


# Train set accuray of our model_1
np.random.seed(77)
layers = (4, 5, 3)
acts = ("relu", "sigmoid")
learning_rate = 0.1
model = init_model(layers, acts)
num_iterations = 10000

print_cost = True
trained_model, costs = train_model(model, X1, Y1, num_iterations, learning_rate, print_cost)

AY, outputs = model_forward(trained_model, X1)
print("AY")
print(AY)
# print("outputs")
# print(outputs)

plot_costs(costs, learning_rate)

p, accuracy = model_accuracy(AY, Y1)
print("Train Accuracy: ", accuracy)
