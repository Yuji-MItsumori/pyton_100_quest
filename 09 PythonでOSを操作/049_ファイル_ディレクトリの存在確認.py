'''
カレントディレクトリないにxyzディレクトリが存在するかを確認しましょう
また、47問目で出力したファイルが存在するか確認してみましょう
'''
import os           # OSライブラリ

# カレントディレクトリないにxyzディレクトリが存在するかを確認
print(os.path.exists('xyz'))
print(os.path.exists('01 文字列'))

# 47問目で出力したファイルが存在するか確認
print(os.path.exists('.\\07 クラス/041_privateとpublic.py'))
