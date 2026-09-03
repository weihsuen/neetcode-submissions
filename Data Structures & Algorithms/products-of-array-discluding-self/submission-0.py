class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre.insert(0,1)

        for i in range(len(nums)-1):
            pre.insert(i+1, pre[i] * nums[i] )

        post = []
        post.insert(0,1)

        for i in range(len(nums)-1,0,-1):
            post.insert(0, (post[0]*nums[i]))


        res = []
        for i in range(len(nums)):
            res.insert(i, pre[i] * post[i])

        return res