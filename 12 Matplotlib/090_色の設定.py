'''
以下のように作成した散布図のマーカの色を(男性: `skyblue`, 女性: `pink`)に変更してください
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

male_ht = np.random.randint(150, 200, size=(50,))
male_wt = np.random.randint(50, 110, size=(50, ))
female_ht = np.random.randint(130, 170, size=(50,))
female_wt = np.random.randint(30, 80, size=(50, ))

# 散布図のマーカの色を(男性: `skyblue`, 女性: `pink`)に変更
plt.scatter(male_ht, male_wt, label='male', color='skyblue')
plt.scatter(female_ht, female_wt, label='female', color='pink')
