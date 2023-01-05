'''
・10をnumで割った時の結果を出力しましょう
・エラーがZeroDivisionErrorだった場合に、エラー内容を出力しましょう
'''

try:
    num = 0
    print(10 / num)
except ZeroDivisionError as e:
    print(e)
