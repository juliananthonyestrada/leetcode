class FileSystem:

    def __init__(self):        
        self.paths = {}

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths:
            return False

        # /neetcode/problems/id/section
        tokens = path.split('/')

        # new src - create it
        if len(tokens) == 2:
            if path not in self.paths:
                self.paths[path] = value
            else:
                return False
        # multiple destinations in path - verify that each dest is in paths
        elif len(tokens) > 2:
            parent_path = '/'.join(tokens[:len(tokens)-1])
            if parent_path not in self.paths:
                return False
            else:
                self.paths[path] = value
        
        return True
     
    def get(self, path: str) -> int:
        return self.paths[path] if path in self.paths else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
