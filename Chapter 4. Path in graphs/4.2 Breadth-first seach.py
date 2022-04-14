from collections import deque
import math
inf=math.inf

def bfs(graph, s):
    dist=[inf for _ in range(len(graph))] #전체 노드에 대해서 거리값을 무한대로 초기화
    dist[s]=0 #자기자신의 노드에 대해서 거리는 0
    queue=deque([s]) #큐에 자기 자신의 값 넣기 

    while(len(queue)!=0): 
        u=queue.popleft() # 앞에서부터 출력 

        for e in graph[u]:
            if dist[e]==inf: # 거리 값이 무한대값이라면 
                queue.append(e) # 큐에 탐색할 노드로 새로 append 
                dist[e]=dist[u]+1 # 거리 1 추가

    return dist

# 그래프 선언(인접리스트)
graph=[[],[2,5],[1,3],[2,5],[5,6],[1,3,4,6],[4,5]]

print(bfs(graph,5)[1:]) #0번째 원소 제외하고 출력