'''
df_peopleに対して、カラム毎のユニーク（固定）な値を抽出してください
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df_people = pd.read_csv('./11 Pandas/people.csv')
print(df_people)

# カラム毎のユニークな値抽出
print(df_people['nationality'].unique())
