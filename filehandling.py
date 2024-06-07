f = open("aa.py","r")
print(f.read())

f = open("alfa.txt", "a")
f.write("i am hemant rawal")
f.close()

f = open("alfa.txt","r")
print(f.read())

a = []
for i in range(1,10,1):
    a.append

f = open("alfa.txt", "w")
f.write("i am hemant rawal 3")
f.close()

f = open("alfa.txt","r")
print(f.read())
f.close()

f = open("alfa.txt","r")
print(f.readline())
f.close()

# f = open ("alfa.txt" "r")
# for x in f:
#     print(x)

import os
print(os.path.abspath('beta.py'))