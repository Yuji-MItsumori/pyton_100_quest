'''
「weather.csv」を読み込み、dfで定義して下さい。

jupyter notebook
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')
print(df)
