"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        intervals.sort(key = lambda k: k.start)

        end_times = []

        for interval in intervals:
            if not end_times or end_times[0] > interval.start:
                count += 1

            else:
                heapq.heappop(end_times) 
            
            heapq.heappush(end_times, interval.end)

        return count
