class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data.get(key, [])
        if len(data) == 0:
            return ""
        
        l, r = 0, len(data) - 1
        while l <= r:
            center = (l + r) // 2
            if data[center][1] == timestamp:
                return data[center][0]
            elif data[center][1] < timestamp:
                l = center + 1
            else:
                r = center - 1
        
        if r < 0: 
            return ""
            
        return data[r][0]      
