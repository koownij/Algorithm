from itertools import combinations
from collections import deque

items = []
for i in range(5):
    for j in range(5):
        items.append((i, j))
        
graph = [list(input()) for _ in range(5)]

cnt = 0
for comb in combinations(items, 7):
    visited = set()
    visited.add(comb[0])
    que = deque()
    que.append(comb[0])
    s = y = 0
    
    while que:
        i, j = que.pop()
        if graph[i][j] == 'S':
            s += 1
        else:
            y += 1
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if (ni, nj) in visited: continue
            if (ni, nj) in comb:
                visited.add((ni, nj))
                que.append((ni, nj))
    
    if s > 3 and s + y == 7:
        cnt += 1
print(cnt)