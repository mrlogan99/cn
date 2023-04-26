'''
Name: Shaikh Mohammad Taha Ameen
Roll No:20CO52
Experiment-3B
Aim:Implementaion of Depth First Search (DFS)
'''

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, '3')

'''

OUTPUT:
Following is the Depth-First Search
3 2 4 8

'''