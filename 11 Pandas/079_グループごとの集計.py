'''
df_irisの下記各クラスにおける
[sepal-lenght][sepal-width][petal-lenght][petal-width]
の平均値を求めて下さい。

・Iris-setosa
・Iris-versicolor
・Iris-birginica
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df_iris = pd.read_csv('./11 Pandas/iris.csv')
print(df_iris.head())

# 平均値
print(df_iris.groupby('Class').mean())

