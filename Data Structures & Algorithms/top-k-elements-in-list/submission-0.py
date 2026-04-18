class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1

        frequent_bucket = [[] for _ in range(len(nums) + 1)] 

        for key in hash_map:
            frequent = hash_map[key]

            curr_arr = frequent_bucket[frequent]
            frequent_bucket[frequent] = curr_arr + [key]


        j = len(nums)
        most_frequent = []
        while k > 0:
            if len(frequent_bucket[j]) == 0:
                j -= 1
                continue

            k -= len(frequent_bucket[j])
            most_frequent += frequent_bucket[j]
            j -= 1
        
        return most_frequent



        