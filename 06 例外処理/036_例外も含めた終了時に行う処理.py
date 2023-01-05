'''
先ほどのdivide()関数で例外処理発生の有無に限らず「全ての処理が終了しました」と表示される様にしましょう
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
    finally:
        print('全ての処理が終了しました')

divide(5, 1)