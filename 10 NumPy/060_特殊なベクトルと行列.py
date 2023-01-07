'''
(8,)のゼロベクトル及び(4,3)のゼロ行列を作成しましょう
また、(5,5)の単位行列も作成しましょう
'''
import numpy as np      # NumPyを使用

# (8,)のゼロベクトルを作成
c = np.zeros(8)
print('\n(8,)のゼロベクトルを作成')
print(c)
print(c.shape)

# (4,3)のゼロ行列を作成
d = np.zeros((4,3))
print('\n(4,3)のゼロ行列を作成')
print(d)
print(d.shape)

# (5,5)の単位行列を作成
print('\n(5,5)の単位行列を作成')
e = np.eye(5)
print(e)
print(e.shape)
