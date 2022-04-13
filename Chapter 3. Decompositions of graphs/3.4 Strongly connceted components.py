def SSCdfs(graph,starts): #SCC DFS 함수 구현
    AllPath=[]
    SSC=[]

    for v in starts: #starts 배열 순서대로 탐색 
        PartPath=[]
        if not visited[v]:

            ss=explore(v,graph)
            PartPath.append(v); PartPath.extend(ss)
            
            AllPath.extend(PartPath)

        if len(PartPath)>0:
            SSC.append(PartPath)

    return SSC, AllPath

def explore(vertex,graph):
    global clock
    searched=[]

    visited[vertex]=True
    pre[vertex]=clock
    clock+=1

    for e in list(graph[vertex]):
        if not visited[e]:
            searched.append(e)
            searched.extend(explore(e,graph))
            
    post[vertex]=clock
    clock+=1

    return searched
    
# 1. 기본설정 : 그래프 선언
graph=[[],[],[1,5],[2,6],[2],[2],[3,5],[5,9],[6,7],[10],[11,12],[8],[11]]

#2. Reverse Graph 생성
def reverseGraph(graph):
    reverse=[[] for _ in range(len(graph))]
    for V in range(1,len(graph)):
        for E in graph[V]:
            reverse[E].append(V) # 기존의 노드와 간선을 바꿔주는 방식
    return reverse

Transpose=reverseGraph(graph) 

print("Reversed: "+str(Transpose))

# 3. 역방향 그래프에 대해서 DFS 수행 

# (1) DFS 수행 전 기본 설정
visited=[False]*(len(graph))
pre=[0] *(len(graph))
post=[0]*(len(graph))
clock=0; 

# (2) DFS 수행
DFSPath=SSCdfs(Transpose,[i for i in range(1,len(graph))])[1] 

# (3) 결과 출력
print("path "+str(DFSPath)) # 역방향 그래프에 대해서 DFS 수행
print("post "+str(post)) #post 넘버 출력 

# 4. 역방향 그래프의 위상 정렬
def TopologySort(graph): 
    LSource=[] # 그래프의 source를 담아두는 리스트

    while(1):
        if graph.count(-1)==len(graph)-1: break

        source=post.index(max(post)) #post 넘버가 가장 큰 수가 해당 그래프의 source가 된다. (소스를 찾음)
        graph[source]=-1; post[source]=-1 #post 넘버 리스트에서 소스의 post 넘버를 -1로 변경 
        
        LSource.append(source) # 소스 리스트에 append 

    return LSource

StartingPoints=TopologySort(Transpose)
print("Starting Points "+str(StartingPoints)) # 이 순서대로 dfs 진행 

# 5. 위상정렬한 starting point에 따라서 DFS 진행 
visited=[False]*(len(graph))
pre=[0] *(len(graph))
post=[0]*(len(graph))
clock=0; 

SCC,AllPath=SSCdfs(graph, StartingPoints)

print("SCC 노드 "+str(SCC))
print("전체 탐색(DFS) "+str(AllPath))