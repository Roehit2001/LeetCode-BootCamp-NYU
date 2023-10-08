class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l=r=0
        while r<len(nums):
            # pops values in queue if smaller
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)
            # Remove left values from window
            while l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            
            r+=1

        return output