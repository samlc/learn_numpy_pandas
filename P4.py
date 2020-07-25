import numpy as np
#dtype定义数组元素数据类型,np.int/np.float/……
a = np.array([[2,3,4],[3,4,5]],dtype=np.int)
print(a)
print(a.dtype,'\n')

#创建一个3行4列的零矩阵
b = np.zeros((3,4),dtype=np.int)
print(b,'\n')

#创建一个3行4列元素全为1的矩阵
c = np.ones((3,4))
print(c,'\n')

#创建一个3行4列元素全为空的矩阵
d = np.empty((3,4))
print(d,'\n')

#创建一个元素从10到20（不含），步长为2的矩阵
e = np.arange(10,20,2)
print(e,'\n')

#创建一个元素从0到12（不含），步长为1的矩阵
f = np.arange(12)
print(f,'\n')

#创建一个元素从0到12（不含），步长为1，3行4列的矩阵
g = np.arange(12).reshape((3,4))
print(g,'\n')

#创建一个元素从1到10（包含），等差均分为5个元素的矩阵
h = np.linspace(1,10,5)
print(h,'\n')

i = np.linspace(1,10,6).reshape((2,3))
print(i,'\n')
