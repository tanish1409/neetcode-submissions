class MedianFinder:

    def __init__(self):
        self.datastream = []
        

    def addNum(self, num: int) -> None:
        self.datastream.append(num)

    def findMedian(self) -> float:
        self.datastream.sort()
        n = len(self.datastream)

        if n%2 == 0:
            return ((self.datastream[n//2] + self.datastream[(n-1)//2])/2)
        else:
            return self.datastream[n//2]
