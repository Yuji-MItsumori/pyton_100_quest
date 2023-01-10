'''
以下の様に「Numpy」でデータを生成して、散布図を作成して下さい
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

data = np.random.randint(0, 50, size=(2,100))

# 散布図を作成
plt.scatter(*data)
