import numpy as np

a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
d = a + b
e = 10*np.sin(a)
f = np.array([[1,1],[0,1]])
g = np.arange(4).reshape((2,2))
#矩阵点乘,i == h
h = np.dot(f,g)
i = f.dot(g)
#随机生成一个元素在0到1之间，2行4列的矩阵
j = np.random.random((2,4))

print(a,b,'\n')
print(b**2,'\n')
print(c,'\n')
print(e,'\n')
print(b<3,'\n')
print(f*g,'\n')
print(h,'\n')
print(i,'\n')
print(j,'\n')
print(np.sum(j),'\n')
print(np.min(j),'\n')
print(np.max(j),'\n')
#当axis值为1时，在每行中寻找;n当axis值为0时，在每列中寻找
print(np.sum(j,axis=0),'\n')
print(np.min(j,axis=1),'\n')
print(np.max(j,axis=0),'\n')
