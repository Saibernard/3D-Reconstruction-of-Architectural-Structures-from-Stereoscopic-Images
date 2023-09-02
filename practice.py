import numpy as np
x = np.array([[1,1,0,1],[2,2,0,2]])
# print(x)
# print(x.shape[0])

X1 = np.array([[1,1,1],[2,2,2],[3,3,3],[4,4,4],[8,9,10]])
X2 = np.array([[2,2,2],[3,3,3],[4,4,4],[5,5,5],[6,6,6]])

print(X1)
Rz_piby2= np.array([[0,-1,0],[1,0,0],[0,0,1]])
print(np.shape(Rz_piby2))

u = (X1[:,2:].T).reshape(5)
print(u)
print(np.shape(u))
v = (X1[:, 2])
print(np.shape(v))

A = np.zeros((X1.shape[0],9))
# print(A)
print(X1.shape[0])
for i in range(X1.shape[0]):
    A[i, 0:3] = X2[i][0] * X1[i]
    A[i, 3:6] = X2[i][1] * X1[i]
    A[i, 6:9] = X2[i][2] * X1[i]

print(np.shape(X1))

c = np.hstack([X1,X2])
print(c)
print(np.shape(c))

x = c[-1, :]
b= x.reshape(3,2)
print(b)


