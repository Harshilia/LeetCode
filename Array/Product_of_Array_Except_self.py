## Problem number - 238
## Difficutly - Medium

def productExceptSelf(nums):
    # Brute Force Approach. 1 test case failed -_-
    # output = []
    # for i in range(len(nums)):
    #     output.append(math.prod(nums[:i]+nums[i+1:]))
    # return output

    multiply = 1
    output = []
    for i in range(len(nums)):
        output.append(multiply)
        multiply = multiply * nums[i]

    multiply = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * multiply
        multiply = multiply * nums[i]
    return output


print(productExceptSelf([1, 2, 3, 4]))

