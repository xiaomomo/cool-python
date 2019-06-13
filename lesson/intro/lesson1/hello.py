# 这是第一行代码，从这行代码开始，我们进入代码的世界了
print("hello world")
# 编程能干啥呢?
# 1. 计算器
print("3+2=",3+2)

# 2. 秘密消息传递
our_message = '这是一个秘密'
secret_message = ''
for char in our_message:
    secret_message += chr(ord(char) + 1)
print(secret_message)

# 3. 获取当前城市信息
import requests
import json
result = json.loads(requests.get('https://api.ip.la/cn?json').text)
print(result['location']['city'])

# 4. 更酷一点的，让电脑唱歌
import os
# 这里可以下载一段音乐
os.system("paplay 1.wav")

