class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:     
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        record = self.store[key]
        left = 0;right = len(record)-1
        ans = ""
        while left <= right:
            mid = left + (right - left)//2
            times,value = record[mid]
            if times <= timestamp:
                ans = value
                left = mid + 1
            else:
                right = mid - 1
        return ans

        
timeMap = TimeMap()
timeMap.set("alice", "happy", 1)
timeMap.set("alice", "sad", 3)
timeMap.get("alice", 1);          
timeMap.get("alice", 2);          
timeMap.set("alice", "sad", 3);   
timeMap.get("alice", 3);  