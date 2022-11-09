class Solution:
    def intToRoman(self, num: int) -> str:
        dic = { 1:"I", 4:"IV", 5:"V", 9:"IX",
               10:"X", 40:"XL", 50:"L", 90:"XC",
               100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        l1 = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        index = math.log(num, 10)
        ans= ''
        for i in range(0, len(l1)):
            t = 1
            while num>=l1[i]:
                ans+=dic[l1[i]]
                num-=l1[i]
           
        return ans