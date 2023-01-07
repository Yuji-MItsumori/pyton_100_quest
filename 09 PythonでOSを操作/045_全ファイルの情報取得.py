'''
カレントディレクトリ内の全てのファイル情報を取得しましょう
'''
import os           # OSライブラリ

# カレントディレクトリ内の全てのファイル情報を取得
for curDir, dirs, files in os.walk('.'):
    for file in files:
        print(f'{curDir}/{file}')

'''
for curDir, dirs, files in os.walk('D:\\00 PRD'):
    for file in files:
        print(f'{curDir}/{file}')
'''
