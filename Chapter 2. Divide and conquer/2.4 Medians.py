
# k=k-1 #list가 0부터 시작하는 것을 감안 
# Sl=[]; Sr=[]; Sv=[]

# for i in S:
#     if i<v: Sl.append(i)
#     elif i==v: Sv.append(i)
#     else: Sr.append(i)

# Sl=sorted(Sl); Sr=sorted(Sr); Sv=sorted(Sv)

# if k<=len(Sl): print(Sl[k])
# elif k>len(Sl) and k<=(len(Sl)+len(Sv)): print(v)
# elif k>len(Sl)+len(Sv): print(Sr[k-len(Sl)-len(Sv)])

S=[2,36,5,21,8,11,20,5,4,1]; v=5; k=8

def selection(S,k):
    k=k-1 #list가 0부터 시작하는 것을 감안 
    Sl=[]; Sr=[]; Sv=[]

    for i in S:
        if i<v: Sl.append(i)
        elif i==v: Sv.append(i)
        else: Sr.append(i)

    if k<=len(Sl): selection(Sl,k)
    elif k>len(Sl) and k<=(len(Sl)+len(Sv)): return v
    elif k>len(Sl)+len(Sv): selection(Sr,k-len(Sl)-len(Sv))

print(selection(S,k))