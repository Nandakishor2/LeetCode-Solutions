class Solution(object):
    def searchInsert(self,nums, target):
    #Declaring start,end variables
        start = 0
        end = len(nums) -1
        while(start <= end):
            mid = (start + end ) // 2

            #Case : mid item is equal to target
            print(start,end,mid)
            if(nums[mid] == target) :
                return mid 
            #Case : mid item is lesser than target
            if(nums[mid] < target):
                start = mid + 1
            #Case : mid item is greater than target
            else: 
                end = mid - 1
        

        #Exit Loop when the target is not found
        return start
    
        
        