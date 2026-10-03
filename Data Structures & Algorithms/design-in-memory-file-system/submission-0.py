class Dir:
    def __init__(self):
        self.children: dict[str, Dir | File] = {}

class File:
    def __init__(self):
        self.content: str = ""

    def add_content(self, new_content):
        self.content += new_content

    def read_content(self):
        return self.content

class FileSystem:
    def __init__(self):
        self.root_dir: Dir = Dir()

    def ls(self, path: str) -> list[str]:
        curr_dir = self.root_dir

        # Root edge case
        if path != "/":
            split_paths = path.split("/")
            for curr_path in split_paths[1 : len(split_paths) - 1]:
                curr_dir = curr_dir.children[curr_path]
            last_path = split_paths[-1]
        else:
            last_path = self.root_dir
            child_arr = []
            for child in curr_dir.children:
                child_arr.append(child)
            return sorted(child_arr)

        if isinstance(curr_dir.children[last_path], File):
            return [last_path]
        else:
            child_arr = []
            for child in curr_dir.children[last_path].children:
                child_arr.append(child)
            return sorted(child_arr)

    def mkdir(self, path: str) -> None:
        curr_dir = self.root_dir
        split_paths = path.split("/")
        for curr_path in split_paths[1:]:
            # Create new dir entry
            if curr_path not in curr_dir.children:
                curr_dir.children[curr_path] = Dir()
            curr_dir = curr_dir.children[curr_path]

    def addContentToFile(self, filePath: str, content: str) -> None:
            curr_dir = self.root_dir
            split_paths = filePath.split("/")
            for curr_path in split_paths[1 : len(split_paths) - 1]:
                curr_dir = curr_dir.children[curr_path]

            file_path = split_paths[-1]
            # Add file to curr_dir
            if file_path not in curr_dir.children:
                curr_dir.children[file_path] = File()
            curr_dir.children[file_path].add_content(content)

    def readContentFromFile(self, filePath: str) -> str:
        curr_dir = self.root_dir
        split_paths = filePath.split("/")
        for curr_path in split_paths[1 : len(split_paths) - 1]:
            curr_dir = curr_dir.children[curr_path]

        file_path = split_paths[-1]
        return curr_dir.children[file_path].read_content()