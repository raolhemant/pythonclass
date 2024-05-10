# number data type
int 
float

#complex
a = 10
a = 11.1
a = 2+3j
print (type(a))
#comparing if its true or not
print(isinstance(a,int))
#string
test = 'git' #single line string
print(type(test))

#multiline string 
Test = '''
abcd
cdef 
ghihk
'''
print(type(Test))

word = 'broadway'
print(word.upper())
print(word.lower())
print(word.title())
print(word.isalpha())

first_name = "sudan"
last_name = " bhandari"
print("my name is ",first_name , "and lastname is",last_name)
#using f string to print the value
print(f'my name is {first_name + last_name} and lastname is {last_name}')