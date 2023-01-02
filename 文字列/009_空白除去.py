# 空白除去
# 「　いつも食べるここのケーキはとても美味しいね。　」
# ※全角スペース

message = '　いつも食べるここのケーキはとても美味しいね。　'
print(message)

print(message.strip())
print(message.lstrip())
print(message.rstrip())

