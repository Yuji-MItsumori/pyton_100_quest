'''
2023年03月28日の日付を取得してください。
'''
from datetime import datetime

dt = datetime(2023, 3, 28, 0, 0, 0, 0)           # 日時を指定して作成
print(f'{dt.year}/{dt.month:02}/{dt.day:02} {dt.hour:02}:{dt.minute:02}:{dt.second:02} {dt.microsecond}')
