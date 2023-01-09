'''
people.csvを読み込みdf_peopleと定義してください
その後、下記の条件を満たすDataFrameをそれぞれ抽出してください

・nationality が America である
・age が 20以上30未満である
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

# people.csvを読み込みdf_peopleと定義してください
df_people = pd.read_csv('./11 Pandas/people.csv')
print(df_people)

# nationality が America である
# print(df_people[df_people['nationality'] == 'America'])
# print(df_people.query('nationality == "America"'))

# age が 20以上30未満である
print(df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)])
print(df_people.query('age >= 20 & age < 30'))
