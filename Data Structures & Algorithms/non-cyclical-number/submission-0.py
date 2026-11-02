class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            summ=0
            nn=[int(i) for i in str(n)]
            for j in nn:
                summ+=j**2
            return summ

        slow=n
        fast=n
        while True:
            slow=square(slow)
            fast = square(square(fast))
            if fast==1:
                return True
            if slow==fast:
                return False
            
        