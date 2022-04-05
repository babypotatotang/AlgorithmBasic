def selection(Sarray,k):
    v=Sarray[int(len(Sarray)/2)] #point 2
    Sl=[]; Sr=[]; Sv=[]

    for i in Sarray:
        if i<v: Sl.append(i)
        elif i==v: Sv.append(i)
        else: Sr.append(i)

    if k<=len(Sl): selection(Sl,k)
    elif k>len(Sl) and k<=(len(Sl)+len(Sv)): print(v); return 0
    elif k>len(Sl)+len(Sv): selection(Sr,k-len(Sl)-len(Sv))

S=[2,36,5,21,8,11,20,5,4,1]; k=8 #point 1
selection(S,k)