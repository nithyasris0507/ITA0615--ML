# Simple Perceptron without libraries

def perceptron_train(data, epochs=10):
    w1, w2, bias = 0, 0, 0
    lr = 0.1

    for _ in range(epochs):
        for x1, x2, label in data:
            y = w1*x1 + w2*x2 + bias
            if label*y <= 0:
                w1 += lr * label * x1
                w2 += lr * label * x2
                bias += lr * label
    return w1, w2, bias

# Load CSV manually
data = []
file = open("iris_simple.csv")
next(file)

for line in file:
    pl, pw, label = line.strip().split(",")
    data.append((float(pl), float(pw), int(label)))

w1, w2, bias = perceptron_train(data)
print("Weights:", w1, w2)
print("Bias:", bias)
