'''
行は先頭のみ、列は、カラム名（列名）が「〇〇.1」「〇〇.2」となっているものを削除したDataFrame dfを再構築して下さい
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')

# 全てのカラム名から、必要なカラム名のみを抽出する(手作業で抽出)
# print(df.columns)
'''
['年月日',
'平均気温(℃)',
'最高気温(℃)',
'最低気温(℃)',
'降水量の合計(mm)',
'最深積雪(cm)',
'平均雲量(10分比)',
'平均蒸気圧(hPa)',
'平均風速(m/s)',
'日照時間(時間)',]
'''
# 列は、カラム名（列名）が「〇〇.1」「〇〇.2」となっているものを削除
df = df[['年月日',
         '平均気温(℃)',
         '最高気温(℃)',
         '最低気温(℃)',
         '降水量の合計(mm)',
         '最深積雪(cm)',
         '平均雲量(10分比)',
         '平均蒸気圧(hPa)',
         '平均風速(m/s)',
         '日照時間(時間)']]
print(df)

# 行は先頭のみ削除
df = df[1:]
print(df)
