class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempDict = dict()
        for x in nums:
            if tempDict.get(x) is None:
                tempDict[x] = 1
            else:
                return True
        return False