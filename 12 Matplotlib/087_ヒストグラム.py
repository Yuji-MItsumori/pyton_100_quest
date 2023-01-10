'''
以下の様に「Numpy」でデータを生成して、ヒストグラムを作成して下さい
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

data = np.random.randint(0, 100, size=(20,))

# ヒストグラムを作成
plt.hist(data, bins=5)
