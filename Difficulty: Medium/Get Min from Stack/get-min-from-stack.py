class Solution:

    def __init__(self):
        # code here
        self.i = []
        self.j = []
        
    # Add an element to the top of Stack
    def push(self, x):
        self.i.append(x)
        if not self.j or x <= self.j[-1]:
            self.j.append(x)
        # code here

    # Remove the top element from the Stack
    def pop(self):
        if self.i:
            if self.i.pop() == self.j[-1]:
                self.j.pop()
        # code here

    # Returns top element of Stack
    def peek(self):
        return self.i[-1] if self.i else -1
        # code here

    # Finds minimum element of Stack
    def getMin(self):
        return self.j[-1] if self.j else -1
        # code here



#{ 
 # Driver Code Starts
# Driver Code
if __name__ == '__main__':
    t = int(input())  # Number of test cases

    for _ in range(t):
        q = int(input())  # Number of queries
        stk = Solution()  # Initialize stack
        results = []

        for _ in range(q):
            query = list(map(int, input().split()))

            if query[0] == 1:
                stk.push(query[1])  # Push operation
            elif query[0] == 2:
                stk.pop()  # Pop operation (no return value)
            elif query[0] == 3:
                results.append(str(stk.peek()))  # Peek operation
            elif query[0] == 4:
                results.append(str(stk.getMin()))  # GetMin operation

        print(" ".join(results))  # Print all results in one line
        print("~")

# } Driver Code Ends