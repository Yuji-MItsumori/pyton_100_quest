'''
下記２つのリストを用意し、それぞれのリストから姓名を同時に出力しましょう
'''
lasts = ['木村', '斎藤', '目黒']
firsts = ['拓哉', '工', '連']

for last, first in zip(lasts, firsts):
    print(last+first)

for fullname in zip(lasts, firsts):
    print(fullname)
