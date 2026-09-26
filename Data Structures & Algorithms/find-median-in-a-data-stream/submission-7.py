class MedianFinder:

    def __init__(self):
        #upper half
        self.min_heap = []
        #lower half
        self.max_heap = []
        self.total = 0

    def addNum(self, num: int) -> None:
        self.total += 1

        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            elem = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, elem)
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
    def findMedian(self) -> float:

        if self.total % 2 == 1:
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0])/2
        
        