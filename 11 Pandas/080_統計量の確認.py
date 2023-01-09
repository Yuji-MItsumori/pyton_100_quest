'''
df_irisの各カラムにおける、下記統計量を算出してください

・平均値
・中央値
・標準偏差
・最大値
・最小値
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df_iris = pd.read_csv('./11 Pandas/iris.csv')

# [sepal-lenght][sepal-width][petal-lenght][petal-width]

# 平均値
print(f'\n平均値\n{df_iris.mean()}')

# 中央値
print(f'\n中央値\n{df_iris.median()}')

# 標準偏差
print(f'\n標準偏差\n{df_iris.std()}')

# 最大値
print(f'\n最大値\n{df_iris.max()}')

# 最小値
print(f'\n最小値\n{df_iris.min()}')
