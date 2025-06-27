class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        # Define the keypad moves
        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        # Initialize DP table: dp[d][l] = number of ways to reach digit d with length l
        dp = [[0] * (n + 1) for _ in range(10)]

        # Base case: 1-length numbers, each digit has 1 way
        for digit in range(10):
            dp[digit][1] = 1

        # Fill DP table
        for l in range(2, n + 1):
            for digit in range(10):
                for neighbor in moves[digit]:
                    dp[digit][l] += dp[neighbor][l - 1]

        # Sum all ways of length n starting from any digit
        total = sum(dp[d][n] for d in range(10))
        return total
