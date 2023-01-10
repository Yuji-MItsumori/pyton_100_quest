'''
以下の様に「Numpy」でデータを生成して「Matplotlib」で折れ線グラフを作成して下さい
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

data = np.random.randint(0, 100, size=(50,2))

# 折れ線グラフを作成
plt.plot(data)
