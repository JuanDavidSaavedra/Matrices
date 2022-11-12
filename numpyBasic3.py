import numpy as np

a = np.array([[2,3,4], [3,-2,4], [1,4,-1]])
b = np.array([20,11,6])

c = np.array([[3,1,-6,3], [-2,7,2,-2], [3,-3,0,-1], [2,1,4,-3]])
d = np.array([3,11,6,5])
f = np.linalg.solve(c,d)

e = np.allclose(np.dot(c,f), d)
print(f,e)

print(np.linalg.solve(a,b))
