'''
Experiment 04
 
Aim:  Implement informed search methods A*.

Code:-'''

import heapq


def astar(start, goal, neighbors_fn, heuristic_fn):
   frontier = [(0, start)]

   came_from = {}
   cost_so_far = {start: 0}

   while frontier:
       _, current = heapq.heappop(frontier)


       if current == goal:
           path = []
           while current != start:
               path.append(current)
               current = came_from[current]
           path.append(start)
           return list(reversed(path))

       for neighbor in neighbors_fn(current):
           new_cost = cost_so_far[current] + 1


           if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
               cost_so_far[neighbor] = new_cost
               priority = new_cost + heuristic_fn(goal, neighbor)
               heapq.heappush(frontier, (priority, neighbor))
               came_from[neighbor] = current


   return None


def neighbors(node):
   x, y = node
   return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def heuristic(goal, node):
   x, y = node
   gx, gy = goal
   return abs(x - gx) + abs(y - gy)

start = (0, 0)
goal = (5, 5)
path = astar(start, goal, neighbors, heuristic)


if path:
   total_cost = len(path) - 1
   print(f"Shortest path: {path}. Total cost: {total_cost}.")
else:
   print("No path found.")

''''
Output:
Shortest path: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]. Total cost: 10.
'''
