'''
以下の２つのパターンで０から９未満の２の倍数が入ったリストを作成しましょう

・空のリストnumsを予め用紙しforループないで.append()関数を用いて要素を追加する
・１行で同様のリストnumbersを作成する
'''

nums = []
print(nums)

# 空のリストnumsを予め用紙しforループないで.append()関数を用いて要素を追加する
for n in range(5):
    nums.append(n * 2)
print(nums)

# １行で同様のリストnumbersを作成する
numbers = [n * 2 for n in range(5)]
print(numbers)
