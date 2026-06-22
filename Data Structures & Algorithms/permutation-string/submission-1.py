class Solution:
   

    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        s1_count = Counter(s1)
        window = Counter(s2[:k])

        if(s1_count==window):
            return(True)
        
        for i in range(k,len(s2)):
            window[s2[i]] += 1

            left = s2[i-k]
            window[left] -= 1

            if(window[left]==0):
                del window[left]
            
            if(s1_count==window):
                return(True)
        return(False)
        