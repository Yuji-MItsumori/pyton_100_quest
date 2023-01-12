'''
下記サイトの「/posts」を用いて、APIを叩いてください
https://jsonplaceholder.typicode.com/

pip install requests

'''
import requests

url = 'https://jsonplaceholder.typicode.com/posts'
res = requests.get(url)

print(res)
print(res.json())
