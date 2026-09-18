import random
# secret_number = 3
# guess = 0

# while guess != secret_number:
#    guess = int(input('Guess the number (1-5): '))
#    if guess != secret_number:
#        print('Wrong! Try again.')

# print('You got it!')

low_num = 1
high_num = 50
answer = random.randint(low_num, high_num)
guesses = 0
is_running = True

print("guess number game!")
print(f"you can select number from {low_num} to {high_num}")
while True:
    guess = input("type a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        print(answer)
        if guess < low_num or guess > high_num:
            print("the number is out of range")
            print(f"you just can select {low_num} to {high_num}")
        elif guess < answer:
            print("too low, try again!")
        elif guess > answer:
            print("too high, try again!")
        else:
            print(f"Correct! the answer is {guess}")
            print(f"number of guesses: {guesses}")
            break

    else:
        print("you can not type a string……")
        print(f"plz select number from {low_num} to {high_num}")
