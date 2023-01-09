'''
dfの５～１０行目、３～６行目（最高気温ｎ（℃）～最深積雪（cm）の要素を取得してください
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')
df = df[['年月日','平均気温(℃)','最高気温(℃)','最低気温(℃)','降水量の合計(mm)','最深積雪(cm)',
         '平均雲量(10分比)','平均蒸気圧(hPa)','平均風速(m/s)','日照時間(時間)']][1:]

df_loc = df.loc[5:10, '最高気温(℃)':'最深積雪(cm)']
df_iloc = df.iloc[4:10, 2:6]
print(df_loc)
print(df_iloc)
