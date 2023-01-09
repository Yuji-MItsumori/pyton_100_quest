'''
iris.csvを読み込みdf_irisと定義して下さい

その後、df_irisのClassカラムにおいて、ユニークな値とその出現回数を確認してください
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

# iris.csvを読み込みdf_irisと定義
df_iris = pd.read_csv('./11 Pandas/iris.csv')
print(df_iris.head())

# df_irisのClassカラムにおいて、ユニークな値とその出現回数を確認
print(df_iris['Class'].value_counts())
