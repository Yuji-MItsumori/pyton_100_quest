'''
先ほどのリストから１つ目の５と最後から３番目の要素を削除しましょう。

numbers = [5, 0, 3, 8, -4, 9, 1, -3, 2]
'''

numbers = [5, 0, 3, 5, 8, -4, 9, 1, -3, 2]
print(numbers)
numbers.remove(5)   # １つ目の５の削除
print(numbers)
numbers.pop(-3)     # 最後から３番目の要素の削除
print(numbers)

# remove()は、リストの先頭から見て、指定した実際の値を削除
# pop()は、指定したインデックス位置に該当する値を削除
