import time

my_time = int(input("Type your time: "))


for x in range(my_time, 0, -1):
    second = x % 60
    minuts = int((x / 60) % 60)
    hours = int(x / 3600)
    print(f"{hours:02}:{minuts:02}:{second:02}")
    time.sleep(1)

print("Time's UP!!!!")
