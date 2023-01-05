'''
次のdivide()関数では変数a,bがそれぞれ数値の場合に正常に数値計算が行われます

aまたはbが文字列の場合（数値の型とは異なる場合）の例外処理（TypeError）をexceptに追加して実装しましょう
'''

def divide(a, b):
    try:
        print(f'計算結果：{a / b}')
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print(e)

divide(5, 0)
