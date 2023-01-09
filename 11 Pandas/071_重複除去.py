'''
nationalityの列に対し、重複がある値の行を削除したDataFrameを取得して下さい
'''
import pandas as pd     # 「pd」の略称はお作法なので推奨される

df_people = pd.read_csv('./11 Pandas/people.csv')
print(df_people)

# nationalityの列に対し、重複がある値の行を削除
print(df_people.drop_duplicates(subset='nationality'))
