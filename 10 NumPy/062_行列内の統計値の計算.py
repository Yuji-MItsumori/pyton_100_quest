'''
以下の行列から合計値、最大値、最小値、平均値、中央値、分散、標準偏差を取得しましょう
'''
import numpy as np      # NumPyを使用

A = np.array(
    [[1, 5, -2],
     [4, 0, -3],
     [-8, 2, 6]])

print(f'Aの合計値　 = {A.sum()}')
print(f'Aの最大値　 = {A.max()}')
print(f'Aの最小値　 = {A.min()}')
print(f'Aの平均値　 = {np.average(A)}')
print(f'Aの中央値　 = {np.median(A)}')
print(f'Aの分散　　 = {np.var(A)}')
print(f'Aの標準偏差 = {np.std(A)}')
