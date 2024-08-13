n=int(input())
arr=list(map(int,input().split()))
largest=arr[0]
for i in range(0,n):
    if arr[i]>largest:
        largest=arr[i]
print(largest)
      
