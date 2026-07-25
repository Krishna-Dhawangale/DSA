class Solution:
    def maxProduct(self, n: int) -> int:
        first_max = 0
        second_max = 0
        
        if n == 0:
            return 0
        
        while n > 0:
            remainder = n % 10
            n = n // 10

            if remainder > first_max:
                second_max = first_max
                first_max = remainder
                
            elif remainder > second_max:
                second_max = remainder

        return first_max * second_max