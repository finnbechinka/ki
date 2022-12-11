import numpy as np
import h5py
import scipy
import sklearn.datasets
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from PIL import Image
from scipy import ndimage
from scipy.special import expit  # expit is the sigmoid function

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
    dZ = dA * s * (1 - s)
    assert dZ.shape == Z.shape

    return dZ

    ### Q : How does the notation exactly work: dZ[Z <= 0] = 0  ?


def plot_costs(costs, learning_rate):
    plt.plot(np.squeeze(costs))
    plt.ylabel("cost")
    plt.xlabel("iterations (per hundreds)")
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()


# Generate data that is not linearly separable
np.random.seed(7)
X1_raw, Y1_raw = sklearn.datasets.make_moons(n_samples=100, shuffle=True, noise=0.1, random_state=None)

# Tip: You can also use other datasets, e.g. sklearn.datasets.make_circles
# Note that the "test your implementation" results in this notebook are calculated using the above dataset.

# Visualize the data:
fig, ax = plt.subplots()
ax.scatter(X1_raw[:, 0], X1_raw[:, 1], marker="o", c=Y1_raw, s=25, edgecolor="k")
plt.show()

# Check and adjust dimensions if necessary
print(X1_raw.shape)
print(Y1_raw.shape)

# We want to have one datapoint per column in X: (2, 100)
# and one label per column in Y : (1, 100)
X1 = np.transpose(X1_raw)
Y1 = Y1_raw.reshape(1, Y1_raw.shape[0])
print(X1.shape)
print(Y1.shape)


def init_params(n_prev, n_curr):
    """
    Arguments:
    n_prev --- size of the previous layer (size of the input of the current layer)
    n_curr --- size of the current layer

    Returns:
    parameters --- (W, b): weight matrix W of shape (n_curr, n_prev), bias vector b of shape (n_curr, 1)
    """

    W = None
    b = None

    return (W, b)


### Q : How to initialize random parameters? Why multiply with 0.01?
### Q : Why is it not a good idea to use zero initialization for the weight matrices? (Hint: symmetry braking)

np.random.seed(42)
(W, b) = init_params(3, 1)
print("W = " + str(W))
print("b = " + str(b))


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
    Z = None
    assert Z.shape == (W.shape[0], A_prev.shape[1])

    # The none-linear part
    if activation == "sigmoid":
        A = None

    elif activation == "relu":
        A = None

    assert A.shape == (W.shape[0], A_prev.shape[1])

    return (Z, A)


np.random.seed(42)
A_prev = np.random.randn(3, 2)
W = np.random.randn(1, 3)
b = np.random.randn(1, 1)

(Z_s, A_s) = forward_step(A_prev, W, b, activation="sigmoid")
(Z_r, A_r) = forward_step(A_prev, W, b, activation="relu")

print("With sigmoid: A = " + str(A_s))
print("With ReLU: A = " + str(A_r))


def compute_cost(Y_hat, Y):
    """
    Arguments:
    Y_hat --- predictions: vector of shape (1, number of examples)
    Y --- labels: vector of shape (1, number of examples)

    Returns:
    cost --- cross-entropy cost
    """

    m = Y.shape[1]  # number of examples

    cost = None

    cost = np.squeeze(cost)  # turns [[17]] into 17
    assert cost.shape == ()

    return cost


Y = np.asarray([[1, 1, 1]])
Y_hat = np.array([[0.8, 0.9, 0.4]])

print("cost = " + str(compute_cost(Y_hat, Y)))


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
        dZ = None

    elif a == "sigmoid":
        dZ = None

    # The linear backward part
    dW = None
    db = None
    dA_prev = None

    assert dA_prev.shape == A_prev.shape
    assert dW.shape == W.shape
    assert db.shape == b.shape

    return (dA_prev, dW, db)


### Q : Give a short explanation of what relu_backward is doing
### Q : What happens when the "axis" parameter of np.sum is set to 1?

np.random.seed(7)
dAL = np.random.randn(1, 2)  # (size of this layer, number of examples)
A_prev = np.random.randn(2, 2)  # (size of prev layer, number of examples)
W = np.random.randn(1, 2)
b = np.random.randn(1, 1)
Z = np.random.randn(1, 2)

(dA_prev, dW, db) = backward_step(A_prev, W, b, "sigmoid", Z, dAL)
print("for sigmoid:")
print("dA_prev = " + str(dA_prev))
print("dW = " + str(dW))
print("db = " + str(db) + "\n")

dA_prev, dW, db = backward_step(A_prev, W, b, "relu", Z, dAL)
print("for relu:")
print("dA_prev = " + str(dA_prev))
print("dW = " + str(dW))
print("db = " + str(db))


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
    W_new = None
    b_new = None

    return (W_new, b_new, a)


np.random.seed(7)
W = np.random.randn(2, 3)
b = np.random.randn(2, 1)
a = "relu"
dW = np.random.randn(2, 3)
db = np.random.randn(2, 1)
(W_new, b_new, a) = update_parameters((W, b, a), (dW, db), 0.1)

print("W_new = " + str(W_new))
print("b_new = " + str(b_new))


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
        (W, b) = None
        model[l] = None

    return model


np.random.seed(7)
model = init_model((2, 3, 1), ("relu", "sigmoid"))
for l in range(1, len(model), 1):
    (W, b, a) = model[l]
    print("Layer", l, ":", W.shape[1], "inputs and", W.shape[0], "outputs ( activation", a, ")")
    print("W: \n", W)
    print("b: \n", b)


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

    assert n == model[1][0].shape[1]  # n == (layer 1 -> W -> number of columns) ?

    costs = []  # to keep track of the cost
    grads = [None for i in range(0, L + 1, 1)]
    grads[0] = (None, None)  # no gradients for input layer 0
    outputs = [None for i in range(0, L + 1, 1)]
    outputs[0] = (None, X)  # "Outputs" of input layer are the datapoints X

    # Loop (gradient descent)
    for i in range(0, num_iterations):

        # Forward propagation
        A_prev = None
        for l in range(1, L + 1, 1):
            (W, b, a) = None
            (Z, A) = None
            outputs[l] = None
            A_prev = None
        AL = None  # Output of last layer L (i.e. predictions)

        # Compute cost
        cost = None

        # Initialize backward propagation by calculating gradients for AL
        dAL = None

        # Backward propagation
        dA = dAL
        for l in range(L, 0, -1):
            (W, b, a) = None
            (Z_prev, A_prev) = None
            (Z, A) = None
            (dA_prev, dW, db) = None
            grads[l] = None
            dA = None

        # Update model parameters
        for l in range(1, L + 1, 1):
            model[l] = None

        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print("Cost after iteration {}: {}".format(i, np.squeeze(cost)))
        if i % 100 == 0:
            costs.append(cost)

    return model, costs

    ### Q : What does np.divide do exactly?


np.random.seed(7)
model = init_model((2, 3, 1), ("relu", "sigmoid"))
num_iterations = 1000
learning_rate = 0.1
print_cost = False
model, costs = train_model(model, X1, Y1, num_iterations, learning_rate, print_cost)
# plot_costs(costs, learning_rate)
for l in range(1, len(model), 1):
    (W, b, a) = model[l]
    print("Layer", l)
    print("W: \n", W)
    print("b: \n", b)


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
        (W, b, a) = None
        (Z, A) = None
        outputs[l] = None
        A_prev = None
    AL = None  # Output of last layer L (i.e. predictions)

    assert AL.shape == (1, X.shape[1])

    return AL, outputs


np.random.seed(7)
model = init_model((2, 3, 1), ("relu", "sigmoid"))
num_iterations = 1000
learning_rate = 0.1
print_cost = False
trained_model, costs = train_model(model, X1, Y1, num_iterations, learning_rate, print_cost)
probabilities, outputs = model_forward(model, X1)
print(probabilities[0, 1:10])
print(Y1[0, 1:10])


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

    # convert probas to 0/1 predictions
    for i in range(0, AL.shape[1]):
        if AL[0, i] > 0.5:
            p[0, i] = 1
        else:
            p[0, i] = 0

    accuracy = np.sum((p == Y) / m)

    return (p, accuracy)


# Train set accuray of our model_1
np.random.seed(77)
model = init_model((2, 5, 1), ("relu", "sigmoid"))
num_iterations = 2000
learning_rate = 0.1
print_cost = True
trained_model, costs = train_model(model, X1, Y1, num_iterations, learning_rate, print_cost)

AY, outputs = model_forward(trained_model, X1)

plot_costs(costs, learning_rate)

p, accuracy = model_accuracy(AY, Y1)
print("Train Accuracy: ", accuracy)
