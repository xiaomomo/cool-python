import random

# theme = random.choice(["地球上", "平行时空", "太空", "上古世界", "银河战舰"])
theme = random.choice(["地球上"])
# gens setting
if theme == "地球上":
    subsetting = random.choice(
        ["美国", "中国", "欧洲", "北朝鲜", "非洲", "中东", "日本", "澳大利亚", "巴哈马群岛"])
    setting = random.choice(
        ["小镇", "大城市", "农场", "学校", "荒野", "郊区",
         "贫民窟", "海洋", "整个世界"])
    setting = subsetting + '的' + setting

    age = random.choice(
        ["新生儿", "蹒跚学步的", "儿童", "未成年", "少年", "青年", "成年", "中年",
         "老年"])
    race = random.choice(["非洲系", "非洲系", "拉美裔", "阿拉伯", "亚洲"])
    gengender = random.randint(0, 100)
    if gengender <= 10:
        gender = ("男性 ")
    if gengender >= 9:
        if gengender >= 47:
            gender = ("男性 ")
        if gengender <= 46:
            gender = ("女性 ")
    protagonist = age + race + gender
    antagonist = random.choice(
        ["一个女生", "一个男生", "一个独裁者", "一个公司", "一个政府", "一个悲剧性的事件", "交通", "宗教",
         "一种疾病", "一个竞争对手", "法律", "一个老朋友", "一只狗"])

conflict = random.choice(
    ["爱上了", "反对", "试图阻止", "试图帮助",
     "尝试探索", "试图逃避"])
end = random.choice(
    ["结果不是太好。", "结果很好。", "最后不幸去世。", "结果永远幸福的生活在一起的。", "这可悲的结束。",
     "这是很光荣的。", "最后，什么也没有改变", "最终放弃了"])
print("在", theme, setting, "有一个", protagonist, "，他", conflict, antagonist, "。", end, sep='')
