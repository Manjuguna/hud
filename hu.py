f=0
m=int(input())
l=list(map(int,input().split()))
for i in range(m) :
    f+=l[i]
h=f/m
print(int(h))
