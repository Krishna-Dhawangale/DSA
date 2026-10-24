class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Numbers of days in every non leap year
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Convert MM-DD to absolute days in years (1-365)
        def date_to_day(date_str: str)-> int:
            month = int(date_str[:2])
            day = int(date_str[3:])
            return sum(days[: month - 1]) + day

        # Convert all 4 dates into day-of-year
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob) 

         # Find the intersection/overlap window
        overlap_start = max(alice_start, bob_start)
        overlap_end = min(alice_end, bob_end)

        # Calculate total days; return 0 if intervals do not overlap
        return  max(0, overlap_end - overlap_start + 1)