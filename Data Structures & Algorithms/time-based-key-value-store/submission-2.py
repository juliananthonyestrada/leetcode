class TimeMap:

    def __init__(self):
        self.nested_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.nested_map:
            self.nested_map[key][timestamp] = value
        else:
            self.nested_map[key] = {}
            self.nested_map[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.nested_map:
            if timestamp in self.nested_map[key]:
                return self.nested_map[key][timestamp]
            else:
                times = list(self.nested_map[key].keys())
                times.sort()

                i = len(times) - 1
                while i > -1:
                    if times[i] > timestamp:
                        i -= 1
                    else:
                        break

                
                if times[i] <= timestamp:
                    return self.nested_map[key][times[i]]         

        return ""

