# -------------------
def new_game():
    guesses = []
    correct_score = 0
    question_num = 1
    for question in questions.keys():
        print("--------------------------")
        print(question)
        for option in options[question_num-1]:
            print(option)
        guess = input("输入你的答案: (A,B,C,D)")
        guess = guess.upper()
        guesses.append(guess)
        correct_score += check_answer(questions.get(question), guess)
        question_num += 1
    display_score(correct_score, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("正确")
        return 1
    else:
        print("错了")
        return 0


def display_score(correct_score, guesses):
    print('--------------------')
    print('------答案揭晓------')
    print('--------------------')

    for i in questions:
        print(questions.get(i), end=" ")
    print()
    for i in guesses:
        print(i, end=" ")
    score = int((correct_score / len(questions)) * 100)
    print(f"你的最终分数是: {score}分")


def play_again():
    response = input("Do you want to play again? (Y/N): ").upper()
    if response == "Y":
        return True
    else:
        return False


questions = {"太阳系中哪个行星是最热的？": "C",
             "陆地上哪个生物是最大的？": "B",
             "森林之王说的是哪个动物": "A",
             "人身上有多少块骨头？": "A",
             "可以给人类呼吸的气体是什么？": "A"}

options = [["A.地球", "B.火星", "C.金星", "D.水星"],
           ["A.蓝鲸", "B.大象", "C.长颈鹿", "D.狮子"],
           ["A.老虎", "B.狮子", "C.豹子", "D.熊"],
           ["A.206", "B.207", "C.208", "D.209"],
           ["A.氧气", "B.氮气", "C.二氧化碳", "D.氩气"]]

new_game()

while play_again():
    new_game()
print("Byeeee!")
