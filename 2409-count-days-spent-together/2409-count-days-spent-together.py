class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        # Numbers of days in every non leap year
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # Convert MM-DD to absolute days in years (1-365)
        def date_to_day(date):
            m, d = map(int, date.split("-"))
            return sum(days[: m - 1]) + d

         # Find the intersection/overlap window
        overlap_start = max(date_to_day(arriveAlice), date_to_day(arriveBob))
        overlap_end = min(date_to_day(leaveAlice), date_to_day(leaveBob))

        # Calculate total days; return 0 if intervals do not overlap
        return  max(0, overlap_end - overlap_start + 1)