import random

graph = []

size = 5
sp_graph = [[" "] * size for i in range(size)]

#1 задание
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)
    
    for n in range(size):
        if (graph[start][n] == 1) and (not (n in visited)):
            dfs(graph, n, visited)
    return visited

#2 задание
def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for i in range(size):
        if type(sp_graph[start][i]) == int and (not (sp_graph[start][i] in visited)):
            dfs2(graph, int(sp_graph[start][i]), visited)
    return visited

#создание матрицы смежностей
for i in range(size):
    graph.append([])
    for j in range(size):
        graph[i].append(0)

for i in range(size):
    for j in range(size):
        f = random.randint(0,1)
        graph[i][j] = f
        graph[j][i] = f

for i in range(size):
    for j in range(size):
        print(f"{graph[i][j]}", end="")
    print()
print()

#создание списка смежностей
ch = 0
for i in range(size):
    ch = 0
    for j in range(size):
            if (graph[i][j] == 1):
                sp_graph[i][ch] = j
                ch += 1
            


for i in range(size):
    for j in range(size):
         print(f"{sp_graph[i][j]}", end="")
    print()
print()

dfs(graph, 0)
print()
dfs2(sp_graph, 0)
