'''
以下のように作成したグラフの軸にタイトル「Height and Weight」と凡例「male, female」を追加してください
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

# タイトル「Height and Weight」
plt.title('Height and Weight')

# 凡例「male, female」
plt.legend()

