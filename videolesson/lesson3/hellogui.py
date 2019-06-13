import easygui

msg = "填写个人信息"
title = "注册"
fieldNames = ["姓名", "手机号"]
fieldValues = []
fieldValues = easygui.multenterbox(msg, title, fieldNames)

print("回答：", fieldValues)
