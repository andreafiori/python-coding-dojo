"""
Unique binary search trees | leetcode 96 | https://leetcode.com/problems/unique-binary-search-trees/
method: dp, use cached results for subtrees of all possible roots

https://leetcode.com/discuss/86650/fantastic-clean-java-dp-solution-with-detail-explaination

"""

class UniqueBinarySearchTrees
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for level in range(2, n + 1):
            for root in range(1, level + 1):
                dp[level] += dp[level - root] * dp[root - 1]
        return dp[n]

    def numTrees(self, n: int) -> int:
        # cache of possible trees
        possibleTrees = [1] * (n + 1)

        # for each number of nodes
        for numNodes in range(2, n + 1):

            # for each possible root
            possibleSubTrees = 0
            for possibleRoot in range(1, numNodes + 1):
                Left = possibleRoot - 1
                Right = numNodes - possibleRoot
                possibleSubTrees += possibleTrees[Left] * possibleTrees[Right]
            possibleTrees[numNodes] = possibleSubTrees

        return possibleTrees[n]
