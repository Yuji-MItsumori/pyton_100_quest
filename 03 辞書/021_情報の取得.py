'''
以下の辞書から次の処理を行いましょう。

・キーのみの表示
・値の中に男性という文字列が存在するか？
・全てのキーと値の表示
'''

dictionary = {
    'A':'光森',
    'B':'祐史',
    'C':'男性',
    'D':'神奈川県',
    'E':'ドラマ鑑賞',
}

# キーのみの表示
print(dictionary.keys())

# 値の中に男性という文字列が存在するか？
print(dictionary.values())
print('男性' in dictionary.values())
print('女性' in dictionary.values())

# 全てのキーと値の表示
for key, value in dictionary.items():
    print(f'KEY = {key}  VALUE = {value}')