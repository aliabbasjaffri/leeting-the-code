class MedianFinder:

    def __init__(self):
        self.arr = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.size += 1

    def findMedian(self) -> float:
        if not self.arr:
            return 
        
        self.arr = sorted(self.arr)
        
        if len(self.arr) % 2 == 0:
            _first = int((self.size -1) /2)
            _second = int((self.size -1)/2) + 1
            return (self.arr[_first] + self.arr[_second])/2
        else:
            return self.arr[int(self.size/2)]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()