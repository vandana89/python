'''lis=list(map(int,input("enter numbers:" ).split()))
lis1=set(lis)
print(lis1)'''
lis=list(map(int,input("enter numbers:" ).split()))
lis1=[]
for i in lis:
    if i not in lis1:
        lis1.append(i)
print(lis1)
        

