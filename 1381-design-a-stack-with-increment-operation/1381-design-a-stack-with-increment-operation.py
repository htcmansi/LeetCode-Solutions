class CustomStack:

    def __init__(self, maxSize: int):
        self.st=[]
        self.maxSize=maxSize
        self.nextindex=0

    def push(self, x: int) -> None:
        if self.nextindex==self.maxSize:
            return 
        self.st.append(x)
        self.nextindex +=1
        

    def pop(self) -> int:
        if self.nextindex==0:
            return -1
        num=self.st.pop()
        self.nextindex -=1
        return num

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if self.nextindex <=i:
                break
            self.st[i] +=val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)