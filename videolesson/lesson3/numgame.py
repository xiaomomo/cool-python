import easygui

# 定义一个题库变量
question_bank = []
# 往题库里放入数字和对应的正确答案
question_bank.append([1, 6, 6, 12, '*++'])
question_bank.append([1, 1, 1, 8, '++*'])
question_bank.append([4, 4, 4, 4, '*++'])
question_bank.append([7, 1, 2, 2, '-**'])
question_bank.append([9, 2, 2, 10, '-*+'])
question_bank.append([7, 2, 1, 10, '**+'])

easygui.msgbox('24点游戏，填写运算符，让4个数字计算得到的结果是24', ok_button='开始游戏')
right_answer = 0
for question in question_bank:
    print('24 nums', question[0:4])
    msg = question[0:4]
    title = "24点"
    fieldNames = ["运算符1", "运算符2", "运算符3"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)
    if ''.join(fieldValues) == question[4]:
        right_answer = right_answer + 1
        easygui.msgbox('恭喜你，答对啦！')
    else:
        easygui.msgbox('很遗憾，打错了，正确答案是' + question[4])
easygui.msgbox('你总共答对了%d道题' % right_answer)
