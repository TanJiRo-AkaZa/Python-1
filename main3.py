l=[4,5,1,2,9,7,10,8]
print("the original list is:",l)
count=0
for i in l:
    count+=i
avg=count/len(l)
print("sum=",count)
print("average=",avg)
l.sort()
print("the smallest number is",l[0])
print("the largest number is",l[-1])