import random

secret_num = random.randint(1, 100)
guess_num = 0
try_time = 0
print('我有一个秘密数字，它在0~99之间，快来猜猜它是多少吧！')
while try_time < 6 and guess_num != secret_num:
    guess_num = int(input('猜它是多少？'))
    if guess_num > secret_num:
        print('大了，再猜猜')
    elif guess_num < secret_num:
        print('小了，再猜猜')
    try_time = try_time + 1

if guess_num == secret_num:
    print('恭喜你，猜对啦！')
else:
    print('很遗憾，你没有猜对，正确数字是', secret_num)


