'''
問題45で行ったパス名の出力を[os.path.join()]で結合してみましょう
'''
import os           # OSライブラリ

# カレントディレクトリ内の全てのファイル情報を取得
for curDir, dirs, files in os.walk('.'):
    for file in files:
#        print(f'{curDir}/{file}')
        # 問題45で行ったパス名の出力を[os.path.join()]で結合
        print(os.path.join(curDir, file))
