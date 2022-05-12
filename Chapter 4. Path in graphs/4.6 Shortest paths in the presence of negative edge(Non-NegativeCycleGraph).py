#Shortest Path
from collections import deque

def update(v,e,dtmp):
    dist[e]=min(dist[e],dist[v]+dtmp)

V=8
graph=[
       [[1,10],[7,8]],
       [[5,2]],
       [[1,1],[3,1]],
       [[4,3]],
       [[5,-1]],
       [[2,-2]],
       [[1,-4],[5,-1]],
       [[6,1]]
       ] #[노드, 가중치]로 그래프 선언

dist=[10**9]*8 # 거리 배열 
dist[0]=0 # 0번 노드를 기준으로 최단 경로 구하기 

path=deque() # 탐색할 노드, 노드 탐색 번지 수 
path.append([0,0])

while 1: 
    v, pivot=path.popleft()
    if pivot==(V-1): 
        break
    for array in graph[v]:
        e=array[0]; dtmp=array[1]
        update(v,e, dtmp)
        path.append([e,pivot+1])

print(*dist)