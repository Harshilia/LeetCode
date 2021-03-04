class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
    
        output = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            
            # store current index and the start index
            current, start = i,i -len(p) + 1  
            
            # update the value of current element in dictionary
            sCounter[s[current]] += 1
            
            # check if the current window matches with desired string
            if pCounter == sCounter:
                output.append(start)
            
            # update the value of start element in dictionary
            sCounter[s[start]] -= 1
            
            # remove the start element if its counter value is 0
            if sCounter[s[start]] == 0:
                del sCounter[s[start]]
                
        return output
            
                    