import random

answer = random.randint(1,100)
number = 0
iter = 0

while(number != answer):
    number = int(input("Enter a number: "))
    if number > answer:
        print("Too high")
    elif number < answer:
        print("Too low")
    iter +=1
print(f"{iter}번 만에 정답!")



