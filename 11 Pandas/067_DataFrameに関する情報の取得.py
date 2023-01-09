'''
下記の値を取得して下さい

・各列のデータ型
・DataFrameのサイズ
・列名
・行名
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')
df = df[['年月日','平均気温(℃)','最高気温(℃)','最低気温(℃)','降水量の合計(mm)','最深積雪(cm)',
         '平均雲量(10分比)','平均蒸気圧(hPa)','平均風速(m/s)','日照時間(時間)']][1:]

print(df.dtypes)    # 各列のデータ型
print(df.shape)     # DataFrameのサイズ
print(df.columns)   # 列名（カラム名）
print(df.index)     # 行名(RangeIndex(start=1, stop=368, step=1):1から、368まで、1刻み)
