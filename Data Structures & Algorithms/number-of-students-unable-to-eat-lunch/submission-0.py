class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        want = [students.count(0), students.count(1)]

        for s in sandwiches:
            if want[s] == 0:
                break
            want[s] -= 1

        return want[0] + want[1]