'''
先ほどのPersonクラスを継承したKidクラスを作成しましょう
その際に自分の年齢を出力する様にクラスメソッドsay_my_name(age)（年齢を引数）を変更しましょう
'''

class Person:
    nationality = '日本'
    def __init__(self, name) -> None:
        self.name = name
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')
    def say_my_name(self):
        print(f'こんにちは、私の名前は{self.name}です')

class Kid(Person):
    def say_my_name(self, age):
        print(f'こんにちは、私の名前は{self.name}です。年齢は{age}歳です')

kid = Kid('みつもりゆうじ')
kid.say_my_name(57)
