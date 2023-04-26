"""
Name : Shaikh Mohammad Taha Ameen
Roll No : 20CO52
"""

def minmax(nodeIndex, maxPlayer, scores):
   if len(scores) == 1:
       return scores[0]


   if maxPlayer:
       return max(
           minmax(nodeIndex * 2, False, scores[: len(scores) // 2]),
           minmax(nodeIndex * 2 + 1, False, scores[len(scores) // 2 :]),
       )


   else:
       return min(
           minmax(nodeIndex * 2, True, scores[: len(scores) // 2]),
           minmax(nodeIndex * 2 + 1, True, scores[len(scores) // 2 :]),
       )




# example scores for testing
scores = [3, 5, 2, 9, 12, 5, 23, 23]


# print the optimal value using the minmax algorithm
print("The optimal value is:", minmax(0, True, scores))


"""
output:- The optimal value is: 12
"""

