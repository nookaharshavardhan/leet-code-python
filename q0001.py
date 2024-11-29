class Solution(object):
    def twoSum(self, nums, target):
        nums_dictonary={} #to store the key values pairs of nums and indexes
        for i,num in enumerate(nums):
            x=target-num
            if x in nums_dictonary:
                return [nums_dictonary[x],i]
            nums_dictonary[num]=i
        return []

lst=[1,2,3,5,6,7,]
hi=Solution(lst,9)
print(hi.twoSum(lst,9))
