from repositories.housework_repository import HouseworkRepository

class HouseworkService:
    def __init__(self):
        self.repository = HouseworkRepository()

    def list_tasks(self, username):
        return self.repository.get_all(username)

    def add_task(self, username, task_name):
        tasks = self.repository.get_all(username)
        if task_name not in tasks:
            self.repository.add(username, task_name)

    def update_task(self, username, old_name, new_name):
        tasks = self.repository.get_all(username)
        if old_name in tasks and new_name not in tasks:
            self.repository.update(username, old_name, new_name)

    def delete_task(self, username, task_name):
        tasks = self.repository.get_all(username)
        if task_name in tasks:
            self.repository.delete(username, task_name)
