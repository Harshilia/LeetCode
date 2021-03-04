class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        dict_freq = {each:nums.count(each) for each in nums}

        output = []

        for each in nums:
            count = 0
            for keys,value in dict_freq.items():
                if each > keys:
                    count = count + value
            output.append(count)
        return output


