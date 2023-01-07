'''
カレントディレクトリ内のファイル情報を取得しましょう
'''
import os           # OSライブラリ

'''
list_dir = os.listdir('.')
print(list_dir)
'''

# カレントディレクトリ内のファイル情報を取得
list_dir = os.listdir('D:\\00 PRD')
print(list_dir)
list_dir.sort()
print(list_dir)
