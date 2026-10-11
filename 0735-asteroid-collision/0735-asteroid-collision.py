class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        st = []

        for i in asteroids:
            while st and i < 0 and st[-1] > 0:
                if st[-1] < abs(i):
                    st.pop()
                    continue

                elif st[-1] == abs(i):
                    st.pop()
                    break
                
                else:
                    break
            else:
                st.append(i)

        return st
