'''
ライブラリ datetimeを用いて現在の日時を取得してください
'''
from datetime import date
from datetime import datetime

dt = datetime.now()                                 # 現在の日時を取得
print(dt)
print(f'{dt.year}/{dt.month:02}/{dt.day:02} {dt.hour:02}:{dt.minute:02}:{dt.second:02} {dt.microsecond}')

to = date.today()
print(to)
