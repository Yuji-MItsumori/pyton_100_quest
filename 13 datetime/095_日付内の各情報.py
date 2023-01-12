'''
現在の日時における、年、月、日、時、分、秒、曜日を取得してください
'''
from datetime import datetime

lst_week = ['月', '火', '水', '木', '金', '土', '日']

dt = datetime.now()                                 # 現在の日時を取得
print(f'今年は{dt.year}年です')                     # 年
print(f'今月は  {dt.month:02}月です')               # 月
print(f'今日は  {dt.day:02}日です')                 # 日
print(f'今日は{lst_week[dt.weekday()]}曜日です')    # 曜日（0:月 1:火 2:水 3:木 4:金 5:土 6:日）
print(f'今は{dt.hour}時です')                       # 時
print(f'今は{dt.minute}分です')                     # 分
print(f'今は{dt.second}秒です')                     # 秒
print(f'今は{dt.microsecond}msです')                # マイクロ秒
