# sci = paper #1
# paper = rock #2
# rock = sci #3
# import random
# n = random.randint(1,3)
# a= '''
# welcome to the game
# 1 = paper
# 2 = sci
# 3 = rock

# '''
# print(a)
# print(n)

# y = (input("enter the value"))
# if y.isdigit():
#     x = int(y)
#     while (n!=x): 
#         if n ==1 and x== 2:
#             print("you won bro!")
#             
#         elif n== 2 and x== 3:
#             print("you won bro!")
#             
#         elif n== 3 and x==1:
#             print("you won bro!")
#             
#         else:
#             print("you lose ")
#             
# else:
#     print("invalid value")

#new practice
# import random
# rock=1
# paper=2
# scissors=3
# for x in range(1,3):
#     cpu_play = random.randint(1,3)
#     # print(cpu_play)
#     x=int(input("Enter your play(1: Rock, 2: Paper, 3: Scissors): "))
#     if(x==cpu_play):
#         print("tie")
#     elif(x==1 and cpu_play==3) or (x==2 and cpu_play==1) or (x==3 and cpu_play==2):
#         print(f"The cpu play is {cpu_play} and your play is {x} so:")
#         print("You win")
#     else:
#         print(f"The cpu play is {cpu_play} and your play is {x} so:")
#         print("you lose")
#     play_again=input("do you want to play again?(yes,no): ")
#     if(play_again!="yes"):
#         


#guess the right game..
import random
x = random.randint(1,20)
y = None
print(x)


guess = 0
while x!= y:
    y = int(input("Enter the value"))
    if x == y:
        print("you guess the right answer")
        
    elif y>x:
        print("please guess the smaller no should be displayed")
        
    elif y < x:
        print("please guess the smaller no should be displayed")
        
    guess = guess + 1

