'''
型変換

以下のデータ型を文字列型に変換しましょう。

int:x = 1
float: x = 1.52
list: x = [1, 2, 0]
dict: x = dict(name = 'john', birth = 'US')
'''

x = 1
print('整数型の文字列変換       = ' + str(x))

x = 1.52
print('浮動小数点型の文字列変換 = ' + str(x))

x = [1, 2, 0]
print('リスト型の文字列変換     = ' + str(x))

x = dict(name = 'john', birth = 'US')
print('辞書型の文字列変換       = ' + str(x))
