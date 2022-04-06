# 기본 함수 선언

def previsit(v):
    global clock
    pre[v]=clock
    clock+=1

def postvisit(v):
    global clock
    post[v]=clock
    clock+=1
    
def explore(G,v):
    visited[v]=True
    searched=[]
    previsit(v)

    for u in list(G[v]): #그래프 v에서 u 노드들이 있음. 
        if not visited[u]:
            searched.append(u)
            searched.extend(explore(G,u))
    postvisit(v)

    return searched

def dfs(graph):
    path=[]
    for v in graph:
        #DFS의 경우 그래프의 가장 첫번째 노드에서부터 순차적으로 탐색을 시작함. 
        if not visited[v]:
             path.append(v)
             path.extend(explore(graph,v))

    return path
    
#기본 세팅 
# 그래프 선언 (유향 그래프)
graph={
    1:[3],
    2:[1,4],
    3:[5,6],
    4:[3],
    5:[],
    6:[]
} 

visited=[False]*(len(graph)+1)
pre=[0] *(len(graph)+1)
post=[0]*(len(graph)+1)
clock=1

path=dfs(graph) #DFS 탐색 경로 
print("Searched Path "+str(path))

LSource=[] # 그래프의 source를 담아두는 리스트

while(1):
    if len(graph)==0: break

    source=post.index(max(post)) #post 넘버가 가장 큰 수가 해당 그래프의 source가 된다. 
    
    del(graph[source]) #그래프에서 소스를 삭제함. 
    post[source]=-1 #post 넘버 리스트에서 소스의 post 넘버를 -1로 변경 
 
    LSource.append(source) # 소스 리스트에 append 
    
print("Topological Sort "+str(LSource))