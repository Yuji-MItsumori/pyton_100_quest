'''
先ほどのnumbersリストの順序を昇順／降順にそれぞれ並び変えましょう。
'''

numbers = [5, 0, 3, 5, 8, -4, 9, 1, -3, -4, 2]
print(numbers)

# 並び替えをした情報で新しくリストを作成する
up_list = sorted(numbers)                   # 昇順
print(up_list)
dw_list = sorted(numbers, reverse=True)     # 降順
print(dw_list)

# numbers自体を並び変える
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
