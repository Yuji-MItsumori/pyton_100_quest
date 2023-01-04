'''
以下の辞書データからpopメソッドを使って、要素Aと要素Bを削除しましょう。
またclearメソッドを使って、全ての要素を削除しましょう。
'''

dictionary = {
    'A':'光森',
    'B':'祐史',
    'C':'男性',
    'D':'神奈川県',
    'E':'ドラマ鑑賞',
}
print(dictionary)

# popメソッドを使って、要素Aと要素Bを削除
dictionary.pop('A')
print(dictionary)
dictionary.pop('B')
print(dictionary)

# clearメソッドを使って、全ての要素を削除
dictionary.clear()
print(dictionary)
