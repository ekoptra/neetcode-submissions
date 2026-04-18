class Solution:    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        
        max_arr_idx = len(nums) - 1
        i = 0
        result = []
        while i <= max_arr_idx:
            j = i + 1
            k = max_arr_idx

            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    while (j < k) and (nums[k] == nums[k-1]):
                        k -= 1
                    
                    while (j < k) and (nums[j] == nums[j+1]):
                        j += 1

                    j += 1
                    k -= 1 
                elif total_sum > 0:
                    k -= 1
                else:
                    j += 1
            
            while (i < max_arr_idx) and (nums[i] == nums[i+1]):
                i += 1
            
            i += 1
        
        return result
                


         