class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q=deque(students)
        j=0
        i=0
        while j<len(q) and i< len(sandwiches):
            if q[0]==sandwiches[i]:
                q.popleft()
                j=0
                i += 1
            else:
                res= q.popleft()
                q.append(res)
                j +=1
        return len(q)
                
            