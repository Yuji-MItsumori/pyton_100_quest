'''
以下の辞書からCとEというキーに対応する値を表示しましょう
'''

dictionary = {
    'A':'光森',
    'B':'祐史',
    'C':'男性',
    'D':'神奈川県',
    'E':'ドラマ鑑賞',
}

# CとEというキーに対応する値を表示
dic_i = dictionary['C']
dic_ig = dictionary.get('C')
print(f'要素Cは{dic_i}{dic_ig}です')

dic_i = dictionary['E']
dic_ig = dictionary.get('E')
print(f'要素Eは{dic_i}{dic_ig}です')

dic_i = dictionary['F']
dic_ig = dictionary.get('F')




