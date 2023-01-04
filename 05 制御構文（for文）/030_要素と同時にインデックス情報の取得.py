'''
下記のリストを用意し、要素とそのインデックスを取得した上で「XX番のYYです」と出力しましょう
例：０番の木村です
'''

lasts = ['木村', '斎藤', '目黒']

for i, last in enumerate(lasts, start=1):
    print(f'{i}番の{last}です')
