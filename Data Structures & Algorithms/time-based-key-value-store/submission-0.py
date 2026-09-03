class TimeMap:

    def __init__(self):
        self.mydict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mydict:
            self.mydict[key] = []

        self.mydict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.mydict.get(key, [])

        l, r = 0, len(values)-1

        while l<=r:
            mid = l + (r-l) //2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r = mid-1

        return res


        
