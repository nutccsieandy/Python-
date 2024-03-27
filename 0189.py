nums=[1,2,3,4,5,6,7]
a=[]
k=int(input("請輸入一個整數(k):"))
s=len(nums)
for i in range(k):
    x=i+1
    a.append(nums[s-x])
a.reverse()
b=set(nums)-set(a)
k1=list(b)
ans=a+k1
print(ans)
