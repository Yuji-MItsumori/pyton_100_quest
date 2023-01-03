'''
次のリストの中から、先頭から２つ目の値と最後の値をそれぞれ出力しましょう。
また２をリストの一番最後に追加しましょう。

numbers = [0, 3, 8, -4, 9, 1]
'''

numbers = [0, 3, 8, -4, 9, 1]
print(numbers)
print(numbers[1])    # 先頭から２つ目の値
print(numbers[-1])   # 最後の値(ネガティブインデックスは、配列の最後からの値)

numbers.append(2)    # ２をリストの一番最後に追加
print(numbers)
