class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        diff = (sumAlice-sumBob)//2
        
        for e in bobSizes:
            if e+diff in aliceSizes:
                return [diff+e, e]