'''
df_peopleの['nationality']カラムをダミー変数に変換して下さい
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df_people = pd.read_csv('./11 Pandas/people.csv')
print(df_people)

# df_peopleの['nationality']カラムをダミー変数に変換
print(pd.get_dummies(df_people, columns=['nationality']))
