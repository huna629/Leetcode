class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        diff = (sumAlice-sumBob)//2
        setAlice = set(aliceSizes)
        setBob = set(bobSizes)
        for e in setBob:
            if e+diff in setAlice:
                return [diff+e, e]