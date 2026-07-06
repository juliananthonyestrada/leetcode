class Solution:
    def simplifyPath(self, path: str) -> str:
        
        directories = []
        path = path.split("/")

        for c in path:
            if c == "" or c == ".":
                continue
            elif c == "..":
                if directories:
                    directories.pop()
            else:
                directories.append(c)
        
        return "/" + "/".join(directories)