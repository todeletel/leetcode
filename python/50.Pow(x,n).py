class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 快速幂  
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = n * -1

        def sub_pow(x, n)-> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            
            if n % 2 == 0:
                return sub_pow(x, n//2) ** 2
            else:
                return sub_pow(x, (n-1)//2) ** 2 * x
        
        return sub_pow(x, n)
