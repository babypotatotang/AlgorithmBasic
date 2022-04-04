#Merge Sort
# import sys
# n = int(input())
# data = [int(sys.stdin.readline().strip()) for i in range(n)]

def sort(a):
    n=len(a)
    if n==1:  
        return a
    elif n>1:
        return merge(sort(a[0:int(n/2)]),sort(a[int(n/2):n]))

def merge(x,y):
    if len(x)==0: return y
    if len(y)==0: return x

    if x[0]<y[0]:
        return x[0:1]+merge(x[1:],y)
    else:
        return y[0:1]+merge(x,y[1:])

input=list(map(int,input().split()))
output=sort(input)
for i in output:
    print(i, end=' ')


