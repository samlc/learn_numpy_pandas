import numpy as np

a = np.arange(14,2,-1).reshape((3,4))
#矩阵a中元素最小值对应的索引
b = np.argmin(a)
#矩阵a中元素最大值对应的索引
c = np.argmax(a)
#矩阵a中所有元素的平均值，d == e == f
d = np.mean(a)
e = a.mean()
f = np.average(a)
#矩阵a中所有元素的中位数
g = np.median(a)
#矩阵a中每个元素累加
h = np.cumsum(a)
#矩阵a中每个元素与后面一个元素的差
i = np.diff(a)
#矩阵a中非零元素的位置
j = np.nonzero(a)
#逐行按从小到大的规则排列矩阵a中元素
k = np.sort(a)
#矩阵a的转置
l = np.transpose(a)
m = a.T
#将矩阵a中所有小于5的元素全部替换成5，将所有大于9的元素全部替换成9
n = np.clip(a,5,9)

print(a,'\n')
print(b,'\n')
print(c,'\n')
print(d,'\n')
print(e,'\n')
print(f,'\n')
print(g,'\n')
print(h,'\n')
print(i,'\n')
print(j,'\n')
print(k,'\n')
print(l,'\n')
print(m,'\n')
print(n,'\n')