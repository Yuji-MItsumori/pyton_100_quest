'''
カレントディレクトリ内にある「09_10_sample.txt」を削除しましょう。
もしファイルがない場合は、以下のコードで作成しましょう
'''
import os           # OSライブラリ

# もしファイルがない場合は、以下のコードで作成
with open('09_10_sample.txt', 'w') as f:
    f.write('これはサンプルです')

# カレントディレクトリ内にある「09_10_sample.txt」を削除
os.remove('09_10_sample.txt')
