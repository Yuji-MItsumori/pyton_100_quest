'''
こちらのdivide()関数でTypeErrorの例外処理が発生した場合、何も処理を行わずスルーしましょう
'''

def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        pass
    finally:
        print('全ての処理が終了しました')

divide(5, '1')