'''
読み込んだdfの先頭３行、末尾１０行を表示して下さい
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')

# print(df.head(3))   # 読み込んだdfの先頭３行表示
print(df.tail(10))  # 読み込んだdfの末尾１０行を表示
