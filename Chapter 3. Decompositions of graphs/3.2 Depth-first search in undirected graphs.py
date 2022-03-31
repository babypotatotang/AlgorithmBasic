#Finding all nodes reachable from a particular node.
def explore(G,v):
    global visited, wish, flag
    visited[v]=True
    if v==wish: 
        flag=True
        return []
    searched=[]

    for u in G[v]: #그래프 v에서 u 노드들이 있음.
        if not visited[u] and not flag:
            searched.append(u)
            searched.extend(explore(G,u))
    return searched

#Depth-first search
def dfs(start):
    searched=[start]
    for vertex in graph:
        if not visited[vertex]: 
            searched.extend(explore(graph,vertex))

    return searched

#python에서는 dictionary 타입으로 graph 선언
graph={
    1:{2,7},
    2:{5,6},
    3:{6},
    4:{},
    5:{2,9},
    6:{2,3},
    7:{1,8},
    8:{7},
    9:{5,10},
    10:{9}
} #무향 그래프의 경우 connected 되어있기만 한다면 해당 엣지를 추가해주어야함. 

visited=[False]*(len(graph)+1)
wish=9 #찾고자하는 노드 
flag=False #발견 플래그
print(dfs(1))