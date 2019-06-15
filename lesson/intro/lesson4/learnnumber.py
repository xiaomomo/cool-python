# # 1. pyton里操作数据
# print(3 + 2)
# print(8 - 3)
# print(2 * 3)
# print(3 / 2)
# # +-*/
# # % **
# print(3 % 2)
# print(2 ** 3)
# # 2. small game
# compute = input("please input your compute")
# while compute != 'q':
#     print("answer:", eval(compute))
#     compute = input("please input your compute")
#
# # 4. 变量 存储数字
# # 变量，记录内存里的数据。在程序运行的过程中不断的发生变化。
# # 讨论，为什么要用变量。游戏得分、生命值、血量、剩余子弹。
# score = 0
# chinese = eval(input("please input chinese score"))
# score = score + chinese
# number = eval(input("please input number score"))
# score = score + number
# english = eval(input("please input english score"))
# score = english + number
# print(score)
#
# # debug turtle画图程序里的变量值。
# import turtle
# pen = turtle.Pen()
# pen.reset()
# # colors = eval(input('please input your colors'))
# colors = ['red', 'yellow', 'green', 'blue', 'grey', 'purple']
# colors_size = len(colors)
# for i in range(360):
#     pen.color(colors[i % colors_size])
#     pen.forward(i * 3 / colors_size + i)
#     pen.left(360 / colors_size + 1)
#     pen.pensize(i * colors_size / 360)
#

# 3. turtle里的数字
# 	1. 多边形
import turtle

pen = turtle.Pen()
pen.reset()
# colors = eval(input('please input your colors'))
slides = eval(input("please input slides"))
size = eval(input("please input size"))
for i in range(slides):
    pen.forward(size)
    pen.right(360 / slides)
turtle.mainloop()

# 	2. 渐变

# 	3. 运算

# 4. 大话变量
# 	1. 手机内存
# 	2. 应用程序杀杀手机就变快了？
# 	3. 变量与应用题

# 5. 大话数字
# 	1. 数字的重要性
# 	2. 计算机里的运算只有加法

# 作业：24点游戏
