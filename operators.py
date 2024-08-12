a=int(input())
b=int(input())
#arithmetic 
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
#relational
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical
a1=True
b1=False
print(a1 and b1)
print(a1 or b1)
print(not(a1))
#bitwise
print(a&b)
print(a|b)
print(a>>b)
print(a<<b)
#membership
a2=[1,2,4]

if 1 in a2:
    print("exists")
else:
    print("not exists")
#identity
a3=10
b3=a3
if a3 is b3:
    print("True")
else:
    print("false")
