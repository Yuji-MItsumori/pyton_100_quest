'''
カレントディレクトリにある「imanyu」フォルダの名前を「mitsumori」に変更しましょう
'''
import os           # OSライブラリ

os.mkdir('imanyu')

# カレントディレクトリにある「imanyu」フォルダの名前を「mitsumori」に変更
os.rename('imanyu', 'mitsumori')
os.remove('mitsumori')
