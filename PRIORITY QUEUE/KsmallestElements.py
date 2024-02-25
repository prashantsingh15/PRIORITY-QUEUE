'''You are given with an integer k and an array of integers that contain numbers in random order.
Write a program to find k smallest numbers from given array. 
You need to save them in an array and return it.
Time complexity should be O(n * logk) and space complexity should not be more than O(k).
Note: Order of elements in the output is not important.'''

import heapq
def kSmallest(lst,k):
    heap=lst[:k] # from 0 th index we have to start it
    heapq._heapify_max(heap)
    n=len(lst)

    for i in range (k,n):
        if heap[0] > lst[i]:
            heapq._heapreplace_max(heap,lst[i])

    return heap

# Main function

n =int(input())
lst=list(int(i) for i in input().strip().split(' '))
k =int(input())
ans = kSmallest(lst,k)
ans.sort()
print(*ans,sep=' ')
