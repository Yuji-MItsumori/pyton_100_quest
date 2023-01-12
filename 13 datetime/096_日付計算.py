'''
一昨日の日付を取得してください
'''
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

today = datetime.today()                # 今日の日付を取得
yestaday = today - relativedelta(days=2)      # ２日前（一昨日）
print(yestaday)

yestaday = today - timedelta(days=2)
print(yestaday)
