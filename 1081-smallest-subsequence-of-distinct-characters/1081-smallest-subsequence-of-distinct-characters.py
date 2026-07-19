class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurence = {}
        seen = set()

        for i, ch in enumerate(s):
            last_occurence[ch] = i

        stack = []

        for i,ch in enumerate(s):
            if ch in seen:
                continue

            while stack and stack[-1] > ch and last_occurence[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)
