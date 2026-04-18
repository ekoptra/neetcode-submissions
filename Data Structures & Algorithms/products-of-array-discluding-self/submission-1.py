class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        suffix_array = []
        len_nums = len(nums)

        prefix_value = None
        suffix_value = None
        for i in range(len_nums):
            j = len_nums - i - 1

            if prefix_value is None:
                prefix_value = 1
            else:
                prefix_value *= nums[i - 1]

            if suffix_value is None:
                suffix_value = 1
            else:
                suffix_value *= nums[j + 1]

            prefix_array.append(prefix_value)
            suffix_array.append(suffix_value)
        

        result = []
        for i in range(len_nums):
            j = len_nums - i - 1
            result.append(prefix_array[i] * suffix_array[j])

        return result

