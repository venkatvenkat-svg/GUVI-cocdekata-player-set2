n=int(input())
sum=0
while(n!=0):
    a1=n%10
    sum=sum+(a1*a1)
    n//=10
print(sum)
