class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        candidate_a = candidate_b = "empty"
        threshold = len(nums) / 3
        cnt_a = cnt_b = 0
        res = []

        for num in nums:
            # matches a curr candidate
            if num == candidate_a:
                cnt_a += 1  # increment
            elif num == candidate_b:
                cnt_b += 1  # increment count
            # open slot
            elif candidate_a == "empty":
                candidate_a = num
                cnt_a += 1
            elif candidate_b == "empty":
                candidate_b = num
                cnt_b += 1
            else:
                cnt_a -= 1
                cnt_b -= 1

                if cnt_a == 0:
                    candidate_a = "empty"
                if cnt_b == 0:
                    candidate_b = "empty"

        cnt_a = cnt_b = 0

        for num in nums:
            if num == candidate_a:
                cnt_a += 1
            elif num == candidate_b:
                cnt_b += 1
    
        if cnt_a > threshold:
            res.append(candidate_a)
        
        if cnt_b > threshold:
            res.append(candidate_b)

        return res
