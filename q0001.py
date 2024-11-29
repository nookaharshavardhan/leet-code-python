class Solution(object):
    def twoSum(self, nums, target):
        nums_dictonary={} #to store the key values pairs of nums and indexes
        for i,num in enumerate(nums):
            x=target-num
            if x in nums_dictonary:#checks in dict which store alredy iterated num
                return [nums_dictonary[x],i]
            nums_dictonary[num]=i
        return []