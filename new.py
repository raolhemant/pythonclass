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
