'''
以下の様に「Numpy」でデータを生成して、２種類の棒グラフ（縦、横）を作成して下さい
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

x = [1, 2, 3, 4, 5]
data = np.random.randint(0, 100, size=(5,))
labels = ['Marht', 'Physics', 'Chemistry', 'Rnglish', 'History']

plt.bar(x, data, tick_label=labels)     # 縦の棒グラフ
plt.barh(x, data, tick_label=labels)    # 横の棒グラフ
