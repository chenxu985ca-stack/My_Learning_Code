# 问卷小游戏
questions = ("太阳系中哪个行星是最热的？",
             "陆地上哪个生物是最大的？",
             "森林之王说的是哪个动物",
             "人身上有多少块骨头？",
             "可以给人类呼吸的气体是什么？")
options = (("A.地球", "B.火星", "C.金星", "D.水星"),
           ("A.蓝鲸", "B.大象", "C.长颈鹿", "D.狮子"),
           ("A.老虎", "B.狮子", "C.豹子", "D.熊"),
           ("A.206", "B.207", "C.208", "D.209"),
           ("A.氧气", "B.氮气", "C.二氧化碳", "D.氩气"))
answers = ('C', 'B', 'A', 'A', 'A')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("请输入你的答案(A,B,C,D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("回答正确！")
    else:
        print("回答错误！")
        print(f"正确答案是：{answers[question_num]}")
    question_num += 1

print('-------------------------')
print('         正确答案         ')
print('-------------------------')

print('你的答案：', end='')
for guess in guesses:
    print(guess, end='')

print()

print('正确答案：', end='')
for answer in answers:
    print(answer, end='')

score = int(score / len(questions) * 100)
print(f"你的最终分数是：{score}")
