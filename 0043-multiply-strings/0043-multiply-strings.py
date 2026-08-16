class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                prod = digit1 * digit2

                p1 = i + j
                p2 = i + j + 1

                total = prod + ans[p2]

                ans[p2] = total % 10
                ans[p1] += total // 10

        start = 0
        while start < len(ans) and ans[start] == 0:
            start += 1

        return "".join(map(str, ans[start:]))


