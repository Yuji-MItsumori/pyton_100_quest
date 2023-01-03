'''
先ほどのnumbersリストの先頭に５を挿入しましょう。
また最後から１つ手前に－３を挿入しましょう。

numbers = [0, 3, 8, -4, 9, 1, 2]
'''

numbers = [0, 3, 8, -4, 9, 1, 2]
print(numbers)
numbers.insert(0, 5)    # 先頭に５を挿入
print(numbers)

numbers.insert(-1, -3)  # 最後から1つ手前に－３を挿入
print(numbers)
