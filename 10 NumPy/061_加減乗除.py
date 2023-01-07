'''
次の計算を行いましょう
'''
import numpy as np      # NumPyを使用

A = np.array([[1, 5],[4, -2]])
B = np.array([[2, -1],[7, 6]])

# 足し算
f = A + B
print('\n足し算')
print(f)

# 引き算
g = A - B
print('\n引き算')
print(g)

# 掛け算
h = np.dot(A, B)
print('\n掛け算')
print(h)

# 割り算（行列同士の演算に割り算はない）
