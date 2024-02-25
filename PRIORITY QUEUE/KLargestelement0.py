'''Given an array A of random integers and an integers k, find and return the kth largest element in the Array.
Note:--> Try to do this question is less than O(N*logN)time 

the first line of input contains an integers ,that denotes it with the symbol N
the following line contain  

'''




import heapq
def kLargest(lst,k):
    heap=lst[:k]
    heapq.heapify(heap)

    n=len(lst)

    for i in range(k,n):
        if heap[0]<lst[i]:
            heapq.heapreplace(heap,lst[i])

    return heap


#main function srart there '

n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k = int(input())
ans = kLargest(lst, k)
print(ans)

