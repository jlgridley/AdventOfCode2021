graph = {}

def addEdge(graph, a, b):
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

with open("input12") as f:
    for line in f:
        a, b = line.strip().split("-")
        addEdge(graph, a, b)
        addEdge(graph, b, a)

print(graph)

def dfs(graph, curr, visited, path):
    if curr == "end":
        # print(path)
        return 1
    if all(node in visited for node in graph[curr]):
        return 0
    path.append(curr)
    if curr.islower():
        visited.add(curr)
    pathsFound = 0
    for node in graph[curr]:
        if node not in visited:
            # print(curr, node, visited, path)
            pathsFound += dfs(graph, node, visited.copy(), path)
        # else:
        #     print(node, visited)
    return pathsFound


print(dfs(graph, "start", set(), []))
