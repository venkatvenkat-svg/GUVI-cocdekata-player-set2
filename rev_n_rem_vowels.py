l=int(input())
s=input()
str = ""
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s: 
    str = i + str
for x in str:
    if x in vowels:
        str=str.replace(x,"")
print(str)
