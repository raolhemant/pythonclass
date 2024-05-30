# sci = paper #1
# paper = rock #2
# rock = sci #3
import random
n = random.randint(1,3)
a= '''
welcome to the game
1 = paper
2 = sci
3 = rock

'''
print(a)
print(n)

y = (input("enter the value"))
if y.isdigit():
    x = int(y)
    while (n!=x):
        if n ==1 and x== 2:
            print("you won bro!")
            break
        elif n== 2 and x== 3:
            print("you won bro!")
            break
        elif n== 3 and x==1:
            print("you won bro!")
            break
        else:
            print("you lose ")
            break
else:
    print("invalid value")

#new practice
# import random
# rock=1
# paper=2
# scissors=3
# for user_play in range(1,4):
#     cpu_play = random.randint(1,3)
#     # print(cpu_play)
#     user_play=int(input("Enter your play(1: Rock, 2: Paper, 3: Scissors): "))
#     if(user_play==cpu_play):
#         print("tie")
#     elif(user_play==1 and cpu_play==3) or (user_play==2 and cpu_play==1) or (user_play==3 and cpu_play==2):
#         print(f"The cpu play is {cpu_play} and your play is {user_play} so:")
#         print("You win")
#     else:
#         print(f"The cpu play is {cpu_play} and your play is {user_play} so:")
#         print("you lose")
#     play_again=input("do you want to play again?(yes,no): ")
#     if(play_again!="yes"):
#         break
