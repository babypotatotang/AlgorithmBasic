#Array
def MakeQueue(key):
    hq=[]
    for i in key:
        hq.append(i)

    return hq

def DecreaseKey(H,V,Vkey):
    H[V]=Vkey
    return H

def DeleteMin(H):
    minV=min(H); minV_index=H.index(minV)
    return minV,minV_index

def dijkstra(graph,s):
    dist=[math.inf for _ in range(len(graph))] #노드 s에서 각 노드들까지의 거리 
    prev=[0 for _ in range(len(graph))]

    dist[s]=0
    H=MakeQueue(dist) #using dist-values as keys

    check=[]

    while H:
        Dist_u, u=DeleteMin(H)
        
        # 실제 Queue에서 delete 하는 대신에 math.inf 값 적용
        check.append(u)
        H[u]=math.inf
        if len(check)==len(graph): break

        if u>0:
            print('노드: '+str(u)+", 거리: "+str(Dist_u))

        for e in graph[u]:
            if dist[e]>dist[u]+lines[u][e]:
                dist[e]=dist[u]+lines[u][e]
                prev[e]=u
                H=DecreaseKey(H,e,dist[e])

dijkstra(graph,1)