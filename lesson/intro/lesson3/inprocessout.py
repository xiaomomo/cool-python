# 1. 回顾一下我们写拼字游戏代码
# 	1. 输入：名字、创造物、形容词
# who = input("please input a name")
# something = input("please input what do you want create")
# describe = input("please descirbe your create with a word")
# 	2. 处理：名字、创造物、形容词的拼接
# result = who + "use python build a " + something + ". it's very " + describe + ". i will be a cool geek!"
# 	3. 输出：在屏幕上显示
# print(result)

# 2. 计算机的核心
# 	1. 看一个过程，然后举例子。 我们让计算机做某事儿，这个过程是怎么发声的呢？我们输入一个信息，计算机收到这个信息后进行加工处理。最后把处理的结果显示给我们。

# 	我们来举几个例子，看看计算机的哪些行为符合这个过程。
# 	拍照、播放音乐、打开网页

# 	3. 输入
# 	计算机的输入设备 键盘、鼠标、触摸屏（即时输入，也是输出）
# 	4. 处理
# 	cpu
# 	5. 输出
# 	计算机的输出设备，显示屏、音响

# 3. 再来改改我们的turtle
# 	1. 可输入
# import turtle
# pen = turtle.Pen()
# color = input('please input your color')
# pen.reset()
# angle = eval(input('please input angle'))
# for i in range(200):
#     pen.color(color)
#     pen.forward(i)
#     pen.right(angle)

# 	2. 更复杂的处理

# import turtle
#
# pen = turtle.Pen()
# colors = eval(input('please input your colors'))
# pen.reset()
# # angle = 360 / len(colors)
# angle = 360 / len(colors) + 1
# for i in range(360):
#     pen.color(colors[i % len(colors)])
#     pen.forward(i)
#     pen.right(angle)

# 	3. 更绚丽的输出

import turtle

pen = turtle.Pen()
pen.reset()
# colors = eval(input('please input your colors'))
colors = ['red', 'yellow', 'green', 'blue', 'grey', 'purple']
colors_size = len(colors)
for i in range(360):
    pen.color(colors[i % colors_size])
    pen.forward(i * 3 / colors_size + i)
    pen.left(360 / colors_size + 1)
    pen.pensize(i * colors_size / 360)

# 4. 脑暴，计算机为什么强大。
# 	1. 家里的其他智能设备
# 		1. 功能单一
# 		2. 不可变
# 		3. 交互简单
# 	2. 计算机
# 		1. 功能丰富
# 		2. 可变
# 		3. 交互复杂

# 作业：可控制的turtle
