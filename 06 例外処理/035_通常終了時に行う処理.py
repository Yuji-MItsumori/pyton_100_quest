'''
先ほどのdivide()関数で例外処理が発生しなかった場合に「正常に終了しました」と表示される様にしましょう
'''

def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print('正常に終了しました')

divide(5, 1)
