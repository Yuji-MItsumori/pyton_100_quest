'''
先ほどのPersonクラス内の変数nationalityを外部から呼び出せないprivateな変数に、
メソッドsay_my_name()も外部から呼び出せないprivateなメソッドに変更しましょう
'''

class Person:
    __nationality = '日本'
    def __init__(self, name) -> None:
        self.name = name
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.__nationality}です')
    def __say_my_name(self):
        print(f'こんにちは、私の名前は{self.name}です')

person = Person('光森祐史')
person.say_hello()
person.__say_my_name()
