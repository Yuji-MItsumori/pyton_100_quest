'''
dfを最高気温が高い順に並び変えて下さい
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df = pd.read_csv('./11 Pandas/weather.csv')
df = df[['年月日','平均気温(℃)','最高気温(℃)','最低気温(℃)','降水量の合計(mm)','最深積雪(cm)',
         '平均雲量(10分比)','平均蒸気圧(hPa)','平均風速(m/s)','日照時間(時間)']][1:]
df.columns = ['年月日','平均気温','最高気温','最低気温','降水量の合計','最深積雪',
              '平均雲量','平均蒸気圧','平均風速','日照時間']

# dfを最高気温が高い順に並び変え
print(df.sort_values('最高気温',ascending=False))   # 降順
print(df.sort_values('最高気温',ascending=True))    # 昇順
