'''
if文を使って以下の処理を実装してください。

int型の変数であるnumを用意し、numが以下の条件の時、
コロン（:）右側の文字列を出力する

・numが正の値の場合：正の値です
・numが０の場合　　：０です
・numが負の値の場合：負の値です
'''

num = -1
if num > 0:
    print('正の値です')
elif num < 0:
    print('負の値です')
else:
    print('０です')

