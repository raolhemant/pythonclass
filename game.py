# import random
# n = random.randint(1,14)
# # print(n)
# num = int(input('guess the number'))
# total_guess = 1
# while(num!=n):
#     total_guess = total_guess+1
#     num = int(input("guess the number"))
# print(f'congratulation your guess is {n}and you guessed{num}')
# print(total_guess)


import random
n = random.randint(1,14)
num = int(input('guess the number: '))
total_guess = 1
print(n)
while(num!=n):
    if total_guess==5:
        print("guess limit reached ")
        break
    num = int(input("guess the number:"))
    total_guess = total_guess+1
if num == n:   
    print(f'congratulation your guess is{total_guess} time ')
