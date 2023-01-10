'''
以下のようにMatplotlibで折れ線グラフを作成し、その結果をPNG形式の画像ファイルで保存して下さい
'''
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

data = np.random.randint(0, 100, size=(50, 2))
plt.plot(data)

# その結果をPNG形式の画像ファイルで保存
plt.savefig('sample.png')
