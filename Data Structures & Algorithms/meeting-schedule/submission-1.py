"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda k: k.start)
        start, end = 0, 0
        for interval in intervals:
            if end <= interval.start:
                end = interval.end
            else:
                return False

        return True