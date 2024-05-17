#arry ma sab datatype same hunu parxa
#list ma j bhaya ni hu xa
test = [1,1,2,3,"hemant"]
print(test)
print(test[2])
a = [2,3,4,5,6,1,2]
b = a[3]
print(f'ths place of {b} and its type is {type(a)}')
print(len(a))
print(a[-1]) #its take value from last

# a = [2,3,3,3,4,5]
# if (a==0 and a<(len(a)-1)):

#slicing
print(a[0:3]) #last data print hudain 3 index ko value aaudaina
print(a[:]) #gives all data 
print(a[1:]) #its gives entire data

#list methon:
#1.append (data always store in last)
student = ['hemant','rawal','alfa']
print(student)
student.append('bijay')
print(student)
#2.insert
student.insert(0,'beta')
print(student)

#delete
# del student
# print(student)# delete entire variable 

# del student[1]
# print(student)

student.pop()
print(student)

a = student.pop()
print(a)

#remove
new = ['slfs','alfa','beta','gama','test','test'] #first ma jo bhetinxa teslai delte garxa 
new.remove('test')
print(new)

#clear
# new.clear()
# print(new)


#concat
new_list = student + new 
print(new_list)

#extends
student.extend(new)
print(student)#we did student in print because student is extend so the value will be given in student 
a = input("what is your name ") 
print(a)