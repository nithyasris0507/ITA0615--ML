# Linear & Logistic Regression without libraries

x = []
y = []

file = open("regression.csv")
next(file)

for line in file:
    a, b = line.strip().split(",")
    x.append(float(a))
    y.append(float(b))

# Linear Regression (y = wx)
w = sum(x[i]*y[i] for i in range(len(x))) / sum(x[i]*x[i] for i in range(len(x)))
print("Linear Regression weight:", w)

# Logistic Regression (Simple sigmoid)
def sigmoid(z):
    return 1 / (1 + (2.718 ** -z))

print("Logistic Regression outputs:")
for val in x:
    print(sigmoid(w * val))
