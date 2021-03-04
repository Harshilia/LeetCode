class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         string_list = [k for k in s]

#         long_string = []
#         len_string = 0
#         for i,each in enumerate(string_list):
#             if each in long_string:
#                 index = long_string.index(each)
#                 del long_string[:index+1]
#                 long_string.append(each)
#             else:
#                 long_string.append(each)
#             len_string = max(len_string,len(long_string))

## EFFICIENT SOLUTION

        # create dictionary for storing element and its index
        store = {}
        max_length=init=0

        for i,each in enumerate(s):
            # if the element already present in the dictionary and start index less than
            # index of the element then we update the start index
            if each in store and init<=store[each]:
                init = store[each] + 1
            else:
                # we calculate the length of the string from start index to current index
                # and compare it with max length
                max_length = max(max_length, i-init+1)

            # store element and its index in the dictionary
            store[each] = i

        return max_length
