# 1. turtle基础
#	1. 找到笔
import turtle

#	2. 拿起笔
pen = turtle.Pen()

#	3. 画线
# pen.forward(100)
#	4. 改变颜色
# pen.color('red')
# pen.forward(100)
#	5. 拐弯
# pen.right(90)
# pen.forward(100)

# 2. 用turtle画图形
#	1. 基础画正方形
#	直行、拐弯；直行、拐弯；直行、拐弯；直行、拐弯
# pen.clear()
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
#	2. 高级画正方形（循环）
# pen.clear()
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

# 3. 画出其他形状
#	1. 有哪些可以变的
#		1. 颜色、长度、角度、边数
# pen.reset()
# pen.color('green')
# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

#		2. 尝试改改重复次数
#			1. 次数调整好大
#			2. 再把角度改改
# pen.reset()
# pen.color('green')
# for i in range(100):
#     pen.forward(100)
#     pen.right(91)

#		3. 来点高级的
#			1. 让长度根据重复次数变化
#			2. 让颜色根据重复次数变化
# color = ['red', 'yellow', 'green', 'blue']
# pen.reset()
# for i in range(200):
#     pen.color(color[i % 4])
#     pen.forward(i)
#     pen.right(91)

# 作业  画一些酷酷的画
# color = ['red', 'yellow', 'green', 'blue']
# pen.reset()
# for i in range(200):
#     pen.color(color[i % 4])
#     pen.forward(i)
#     pen.right(61)
