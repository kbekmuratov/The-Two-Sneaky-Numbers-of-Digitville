from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        output = []  
        seen = set()  
        duplicates = set()  

        for i in nums:
            if i in seen and i not in duplicates:  
                output.append(i)
                duplicates.add(i)
            else:
                seen.add(i) 
        return output
