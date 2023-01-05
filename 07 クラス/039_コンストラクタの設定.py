'''
先ほどのPersonクラスにコンストラクタ（インスタンス生成時に呼び出される関数）を使って、
引数に名前を設定してnameというインスタンス変数を持たせましょう。
またsay_my_name()という自分の名前を出力するクラスメソッドを実装しましょう
'''

class Person:
    nationality = '日本'
    def __init__(self, name) -> None:
        self.name = name
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')
    def say_my_name(self):
        print(f'こんにちは、私の名前は{self.name}です')

person = Person('光森祐史')
person.say_hello()
person.say_my_name()
