'''
本日の日付を2021/07/01 のような形式に変換してください。
'''
import datetime

today = datetime.date.today()
print(f'{today.year}/{today.month:02}/{today.day:02}')
print(today.strftime('%Y/%m/%d'))
