
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
