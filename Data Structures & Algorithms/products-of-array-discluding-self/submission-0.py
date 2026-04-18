class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_product_result = 1
        number_of_zero = 0

        for n in nums:
            if n == 0:
                number_of_zero += 1
            else:
                all_product_result *= n

        
        result = []
        for n in nums:
            if number_of_zero > 1:
                result.append(0)
            elif number_of_zero == 1:
                if n == 0:
                    result.append(all_product_result)
                else:
                    result.append(0)
            else:
                result.append(int(all_product_result / n))
        
        return result