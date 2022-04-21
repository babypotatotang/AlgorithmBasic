import math

# heap 형태를 만드는 함수 
def heapify(tree,n,index):
    Smallest=index #부모노드의 index를 가장 작다고 가정
    
    Left=2*index+1; Right=2*index+2
	
    #Smallest의 value가 각각 left, right보다 큰 경우 갱신
    if Left<n and tree[Smallest][1]>tree[Left][1]:
        Smallest=Left
    if Right<n and tree[Smallest][1]>tree[Right][1]:
        Smallest=Right
    
    #Smallest가 갱신되었다면 
    if Smallest != index:
    	#swap
        tree[Smallest],tree[index]=tree[index],tree[Smallest]
        #다시 heapify
        heapify(tree,n,Smallest)

def MakeQueue(key):
    n=len(key)
    tree=[[0,0]]*n
    for i in range(n):
        tree[i]=[i,key[i]]

    for index in range((n//2)-1,-1,-1):
        heapify(tree,n,index)
    return tree

def DecreaseKey(tree,KeyNum,KeyValue):
    n=len(tree)
    
    for i in range(n):
        if tree[i][0]==KeyNum:
            tree[i][1]=KeyValue
            
    for index in range((n//2)-1,-1,-1):
        heapify(tree,n,index)

    return tree

def DeleteMin(tree):
    minNode=tree.pop(0)

    minIndex=minNode[0]; minValue=minNode[1]
    return minValue,minIndex

def dijkstra(graph,s):
    dist=[math.inf for _ in range(len(graph))] #노드 s에서 각 노드들까지의 거리 
    prev=[0 for _ in range(len(graph))]

    dist[s]=0
    H=MakeQueue(dist) #using dist-values as keys

    while H:
        Dist_u,u=DeleteMin(H)
        if u>0:
            print('노드: '+str(u)+", 거리: "+str(Dist_u))
        for e in graph[u]:
            if dist[e]>dist[u]+lines[u][e]:
                dist[e]=dist[u]+lines[u][e]
                prev[e]=u
                H=DecreaseKey(H,e,dist[e])

##Main##
graph=[[],[2,3],[3,4,5],[2,4,5],[],[4]]
lines=[[0 for j in range(len(graph))] for i in range(len(graph))]
lines[1][2]=4; lines[1][3]=2; lines[2][3]=3; lines[2][4]=2; lines[2][5]=3; lines[3][2]=1; lines[3][4]=4; lines[3][5]=5; lines[5][4]=1
for i in range(len(graph)):
    for j in range(len(graph)):
        if i!=j and lines[i][j]==0:
            lines[i][j]=math.inf

dijkstra(graph,1)
