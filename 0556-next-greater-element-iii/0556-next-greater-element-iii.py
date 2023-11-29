class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        i = len(arr)-1
        #decreasing pattern 4321
        while i-1>=0 and arr[i]<=arr[i-1]:
            i-=1
        if i==0: return -1
        
        j=i
        while j+1<len(arr) and arr[j+1]>arr[i-1]:
            j+=1
            
        arr[i-1], arr[j] = arr[j], arr[i-1] #swap elements
        arr[i:]=arr[i:][::-1] #reverse digits after i-1
        
        ans = int(''.join(arr))
        return ans if ans<1<<31 else -1