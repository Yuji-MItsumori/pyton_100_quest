'''
jsonモジュールを使って以下のjsonファイルを読み込みましょう
'''

import json

with open('./08 ファイル操作/sample.json', 'r') as f:
    # jsonモジュールを使って以下のjsonファイルを読み込み
    data = json.load(f)

#print(data)
#print(data['store_name'])
print(data['items'])
