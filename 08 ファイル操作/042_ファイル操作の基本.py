'''
下記のテキストファイルを用意し、
テキストファイルからテキストデータを取得して出力しましょう
※read(), close()メソッドを使用する方法

f = open(ファイルパス, モード)					
モード	'r'		読み込み（デフォルト）
		'w'		書き込み
		'a'		追記
		'r+'	読み込み＋書き込み

from pathlib import Path
path = Path.cwd()
print(path)
'''

f = open('./08 ファイル操作/sample.txt')
read_str = f.read()
print(read_str)
f.close()
