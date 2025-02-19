#User function Template for python3
class Solution:
    def mergeKLists(self, arr):
        if not arr:   return None
        def merge(i, j):
            if not i:  return j
            if not j:  return i
            if i.data < j.data:
                i.next = merge(i.next, j)
                return i
            else:
                j.next = merge(i, j.next)
                return j
                
        while len(arr) > 1:
            k = []
            for i in range(0, len(arr), 2):
                k.append(merge(arr[i], arr[i + 1] if i + 1 < len(arr) else None ))
            arr = k
        return arr[0]
#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends