'''
Personクラスを用意し、クラス変数としてnationality: 'japan'、
クラスメソッドとしてsay_hello()を実装しましょう
say_hello()メソッドでは「こんにちは、私の国籍は〇〇です。」
と出力する様にしましょう。なお、〇〇には国籍名（nationality）が入ります
'''

class Person:
    nationality = '日本'
    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')

person = Person()
person.say_hello()
