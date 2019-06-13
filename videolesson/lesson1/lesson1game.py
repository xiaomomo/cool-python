# 定义一个题库变量
question_bank = []
# 往题库里放入数字和对应的正确答案
question_bank.append([1, 6, 6, 12, '*++'])
question_bank.append([1, 1, 1, 8, '++*'])
question_bank.append([4, 4, 4, 4, '*++'])
question_bank.append([7, 1, 2, 2, '-**'])
question_bank.append([9, 2, 2, 10, '-*+'])
question_bank.append([7, 2, 1, 10, '**+'])

right_answer = 0
for question in question_bank:
    print('24 nums', question[0:4])
    operators = input('input three operators')
    if operators == question[4]:
        right_answer = right_answer + 1
        print('good,you are right!')
    else:
        print('so bad, the right answer is ', question[4])
print('you answer %d nums' % right_answer)
