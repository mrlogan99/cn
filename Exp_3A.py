'''
Name: Shaikh Mohammad Taha Ameen                                                                          
Roll No:20CO52
Experiment-3A
Aim:Implementaion of Breadth First Search (BFS)

'''

graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = []
queue = []     

def bfs(visited, graph, node, goal): 
  visited.append(node)
  queue.append(node)

  while queue:  
    a=goal
    m = queue.pop(0) 
    print(m,end=" ")
    if(m==a):
        
        break    

    for i in graph[m]:
      if i not in visited:
        visited.append(i)
        queue.append(i)


print("Following is the Breadth-First Search")
bfs(visited, graph, '5', '8')   

'''
OUTPUT:
Following is the Breadth-First Search
5 3 7 2 4 8
'''
