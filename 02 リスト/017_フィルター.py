'''
次の、偶数のみを返す関数とfilter()を用いて先ほどのnumbersリストから
偶数のみを取り出したリストを作成しましょう。
'''

numbers = [5, 0, 3, 5, 8, -4, 9, 1, -3, 2]
print(numbers)

def isEven(number):
    if number % 2 == 0:
        print(f'This number, {number} is even!')
        return True
    else:
        print(f'This number, {number} is odd!')
        return False

# 偶数のみを取り出したリストを作成
ret_list = list(filter(isEven, numbers))
print(ret_list)
