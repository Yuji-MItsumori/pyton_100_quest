'''
先ほどのテキストデータを取得する処理をwith構文を使って実装しましょう。
'''

# 先ほどのテキストデータを取得する処理をwith構文を使って実装
with open('./08 ファイル操作/sample.txt', 'r') as f:
    read_str = f.read()
    print(read_str)
