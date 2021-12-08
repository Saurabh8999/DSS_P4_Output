from sklearn import datasets

iris = datasets.load_iris()

X = iris.data[:, :2]
# we only take the first two features.

y = iris.target
print(X)

print("Targets are", y)