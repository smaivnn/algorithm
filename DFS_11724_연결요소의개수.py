import sys;
sys.setrecursionlimit(10000);
input = sys.stdin.readline

n, m = map(int, input().split());
graph = [[] for _ in range(n+1)];
visited = [False] * (n+1);
count = 0;

def dfs(v) :
    visited[v] = True; # 방문처리
    for i in graph[v] : # v와 연결된 노드들을 탐색
        if not visited[i] :
            dfs(i);

for _ in range(m) :
    u, v = map(int, input().split());
    # 양방향 그래프이므로 양쪽에 모두 추가
    graph[u].append(v);
    graph[v].append(u);

for i in range(1, n+1) :
    if not visited[i] :
        count += 1;
        dfs(i);

print(f"{count}");
        