class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            digit = n
            while digit > 0:
                prod *= (digit % 10)
                digit //= 10

            if prod % t == 0:
                return n

            n += 1