'''
以下の行列に逆行列がある場合、その行列を求めましょう
'''
import numpy as np      # NumPyを使用

A = np.array([[1, 5],[4, -2]])

print(f'逆行列が存在するかどうかを確認  {np.linalg.det(A)}')
A_inv = np.linalg.inv(A)
print(f'逆行列\n{A_inv}')
print(f'\n{np.dot(A, A_inv)}')

