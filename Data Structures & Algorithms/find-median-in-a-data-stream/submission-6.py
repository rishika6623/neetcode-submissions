class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap and not self.max_heap:
            heapq.heappush(self.min_heap, -num)

        elif not self.min_heap:
            num_max = heapq.heappop(self.max_heap)
            if num_max < num:
                heapq.heappush(self.min_heap, -num_max)
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, -num)
                heapq.heappush(self.max_heap, num_max)

        elif not self.max_heap:
            num_min = -heapq.heappop(self.min_heap)
            if num_min > num:
                heapq.heappush(self.min_heap, -num)
                heapq.heappush(self.max_heap, num_min)
            else:
                heapq.heappush(self.min_heap, -num_min)
                heapq.heappush(self.max_heap, num)

        else:
            #find top of min heap (max elem)
            num_min = -heapq.heappop(self.min_heap)

            #find top of max heap (min elem)
            num_max = heapq.heappop(self.max_heap)

            #push onto right one
            if num_min > num:
                heapq.heappush(self.min_heap, -num)
                heapq.heappush(self.max_heap, num_max)
                if len(self.min_heap) <= len(self.max_heap):
                    heapq.heappush(self.min_heap, -num_min)
                else:
                    heapq.heappush(self.max_heap, num_min)
            elif num_max < num:
                heapq.heappush(self.max_heap, num)
                heapq.heappush(self.min_heap, -num_min)
                if len(self.min_heap) <= len(self.max_heap):
                    heapq.heappush(self.min_heap, -num_max)
                else:
                    heapq.heappush(self.max_heap, num_max)
            else:
                heapq.heappush(self.min_heap, -num_min)
                heapq.heappush(self.max_heap, num_max)
                if len(self.min_heap) >= len(self.max_heap):
                    heapq.heappush(self.max_heap, num)
                else:
                    heapq.heappush(self.min_heap, -num)


    def findMedian(self) -> float:
        #print(self.min_heap, self.max_heap)
        if len(self.min_heap) < len(self.max_heap):
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, num)
            return num
        elif len(self.max_heap) < len(self.min_heap):
            num = -heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, -num)
            return num
        else:
            num = heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, num)
            num2 = -heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, -num2)
            return (num2 + num)/2