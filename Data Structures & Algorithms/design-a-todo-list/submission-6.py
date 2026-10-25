class Task:
    def __init__(self, userId: int, dueDate: int, tags:  List[str], desc: str, task_idx: int):
        self.userId = userId
        self.dueDate = dueDate
        self.tags = tags
        self.desc = desc
        self.task_idx = task_idx
        self.finished = False


class TodoList:
    def __init__(self):
        self.global_idx = 1
        self.tasks: List[Task] = []

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        self.tasks.append(Task(userId, dueDate, tags, taskDescription, self.global_idx))
        self.global_idx += 1

        return self.global_idx - 1
    
    def getAllTasks(self, userId: int) -> List[str]:
        descriptions = []
        for t in sorted(self.tasks, key=lambda t: t.dueDate):
            if t.userId == userId:
                descriptions.append(t.desc)
        
        return descriptions

    
    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        descriptions = []
        for t in sorted(self.tasks, key=lambda t: t.dueDate):
            if t.userId == userId and tag in t.tags:
                descriptions.append(t.desc)
        
        return descriptions    
        
    def completeTask(self, userId: int, taskId: int) -> None:
        for task in self.tasks:
            if task.userId == userId and task.task_idx == taskId:
                self.tasks.remove(task)
                return
        





