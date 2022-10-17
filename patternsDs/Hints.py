"""
1.Whenever it is mentioned in the question that we need to find
Largest /Smallest SubArray Then there could a a case for sliding
Window Appraoch
->Hint Problem statement =="In many problems dealing with an array (or a LinkedList),
we are asked to find or calculate something
among all the subarrays (or sublists) of a given size"

2.Whenever it is mentioned in the question that we need to find
pairs,triplets etc. then there could be a case of Two Pointers
Approach

Hint Problem Statements = "In problems where we deal with sorted arrays
(or LinkedLists) and need to
find a set of elements that fulfill certain constraints,
the Two Pointers approach becomes quite useful.
The set of elements could be a pair, a triplet or even a subarray."

"""

import heapq

list =[]
heap=heapq.heapify(list)
for i in range(len(arr)):
    if len(heapq) >k:
        heap.heappop()
    else:
        heap.push(-1*arr[i])
return -1* heap[0]