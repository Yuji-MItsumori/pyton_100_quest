'''
45問目で取得したファイルの絶対パスを出力しましょう
'''
import os           # OSライブラリ

# 45問目で取得したファイルの絶対パスを出力
file_path = os.path.abspath('.\07 クラス/041_privateとpublic.py')
print(file_path)
