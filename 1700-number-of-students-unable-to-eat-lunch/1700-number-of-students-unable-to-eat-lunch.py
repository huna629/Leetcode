from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        index = 0
        while index<len(students) and count[sandwiches[index]]:
            count[sandwiches[index]]-=1
            index +=1
        return len(students)-index