# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder(object):

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap , -num)
        heapq.heappush(self.min_heap , -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap , -heapq.heappop(self.min_heap))
       
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        return (self.min_heap[0] + (-self.max_heap[0]))/2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()