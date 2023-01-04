'''
26問目の処理に追加でnum==3の時のみ出力結果が出ない様に実装しましょう
'''

for num in range(10):
    if num == 3:
        continue
    print(num)
