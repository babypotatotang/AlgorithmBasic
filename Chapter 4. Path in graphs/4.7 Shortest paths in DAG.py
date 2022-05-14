import numpy as np
# 선언 및 초기화
inf=np.inf
Graph=[
        [],
        [[2,7],[5,4]],
        [[4,1],[5,5]],
        [[1,2],[2,6]],
        [],
        [[4,-2]],
        [[1,3],[3,-1]]
]
N=6 #노드의 개수 
dist=[inf]*(N+1)
dist[1]=0

#Linearize Sort
#(1) Calculate Degree
degree=[0]*(N)
for vs in Graph: 
    for vnodes in vs:
        vnode=vnodes[0]
        degree[vnode-1]+=1

#(2) Sort 
sorts=[[i,degree[i]] for i in range(N)]
sorts=sorted(sorts,key=lambda s:s[1])
order=[o[0]+1 for o in sorts]

# Update the dist
for v in order:
    for e in Graph[v]:
        enode=e[0]; dtmp=e[1]
        dist[v]=min(dist[v],dist[enode]+dtmp)
dist=dist[1:]
print(*dist)