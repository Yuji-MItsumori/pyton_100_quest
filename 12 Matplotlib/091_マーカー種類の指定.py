'''
以下のように作成したグラフのマーカーを(男性: `▷`, 女性: `◁`)に変更してください
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

male_ht = np.random.randint(150, 200, size=(50,))
male_wt = np.random.randint(50, 110, size=(50, ))
female_ht = np.random.randint(130, 170, size=(50,))
female_wt = np.random.randint(30, 80, size=(50, ))

# ーカーを(男性: `▷`, 女性: `◁`)に変更
plt.scatter(male_ht, male_wt, label='male', marker='>')
plt.scatter(female_ht, female_wt, label='female', marker='<')
