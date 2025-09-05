
#40. Combination Sum II
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backTrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backTrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backTrack([],0,target)
        return res


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [10,1,2,7,6,1,5]
    target = 8
    print("Output is:", sol.combinationSum2(nums, target))
