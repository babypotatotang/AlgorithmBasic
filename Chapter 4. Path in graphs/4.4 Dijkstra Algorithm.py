# 그래프 선언
import math
import heapq

def DecreaseKey(H,V,Vkey):
    for i in range(len(H)):
        if H[i][1]==V:
            H[i][0]=Vkey
    heapq.heapify(H)
    
    return H


def MakeQueue(key):
    hq=[]

    for d in range(len(key)):
        heapq.heappush(hq,[key[d],d])

    return hq

def DeleteMin(H):
    return heapq.heappop(H)

def dijkstra(graph,s):
    dist=[math.inf for _ in range(len(graph))] #노드 s에서 각 노드들까지의 거리 
    prev=[0 for _ in range(len(graph))]

    dist[s]=0
    H=MakeQueue(dist) #using dist-values as keys

    while H:
        Dist_u, u=DeleteMin(H)
        if u>0:
            print('노드: '+str(u)+", 거리: "+str(Dist_u))

        for e in graph[u]:
            if dist[e]>dist[u]+lines[u][e]:
                dist[e]=dist[u]+lines[u][e]
                prev[e]=u
                H=DecreaseKey(H,e,dist[e])

graph=[[],[2,3],[3,4,5],[2,4,5],[],[4]]
lines=[[0 for j in range(len(graph))] for i in range(len(graph))]
lines[1][2]=4; lines[1][3]=2; lines[2][3]=3; lines[2][4]=2; lines[2][5]=3; lines[3][2]=1; lines[3][4]=4; lines[3][5]=5; lines[5][4]=1
for i in range(len(graph)):
    for j in range(len(graph)):
        if i!=j and lines[i][j]==0:
            lines[i][j]=math.inf

dijkstra(graph,1)