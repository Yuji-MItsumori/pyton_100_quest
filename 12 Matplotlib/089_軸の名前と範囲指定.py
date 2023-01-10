'''
以下のように作成したグラフの軸に
タイトル(x軸: Height[cm], y軸: Weight [kg])と
範囲(x軸: 110〜210, y軸: 20〜120)を追加してください
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

male_ht = np.random.randint(150, 200, size=(50,))
male_wt = np.random.randint(50, 110, size=(50, ))
female_ht = np.random.randint(130, 170, size=(50,))
female_wt = np.random.randint(30, 80, size=(50, ))

plt.scatter(male_ht, male_wt, label='male')
plt.scatter(female_ht, female_wt, label='female')

# タイトル(x軸: Height[cm], y軸: Weight [kg])
plt.xlabel('Height[cm]')
plt.ylabel('Weight [kg]')

# 範囲(x軸: 110〜210, y軸: 20〜120)
plt.xlim(110, 210)
plt.ylim(20, 120)
