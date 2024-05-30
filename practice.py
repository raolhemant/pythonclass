#finding the sum of positive number using recursion
def pos(n):
    sum = 0
    if not n:
        return 0
    elif n[0]>0:
        return n[0] + pos(n[1:])
    else:
        return pos(n[1:])
    
n = [1, 2, 4, -4, 5, 6, -7]
print("Sum of positive numbers:", pos(n))

#finding the fibonacci series of 10 terms using recursion

#function to add two number
def sum():
    n = 1
    x = 2
    sums = n + x
    print(sums)
sum()

#using function take weither the number is armstrong or not..
def arms():
    x = int(input("enter the value"))
    temp = x
    r = x%10
    sum = sum + r*r*r
    x = x%10
    if 