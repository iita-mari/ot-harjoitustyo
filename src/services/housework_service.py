from repositories.housework_repository import HouseworkRepository

class HouseworkService:
    """Service class for housework-related things.
    """

    def __init__(self):
        self.repository = HouseworkRepository()

    def list_tasks(self, username):
        """Lists all tasks (houseworks) of the user

        Args:
            username: Name of the user

        Returns:
            list of tasks: Returns user's task (housework) list
        """

        return self.repository.get_all(username)

    def add_task(self, username, task_name):
        """Add task (housework) to user's list

        Args:
            username: Name of the user
            task_name: Name of the task (housework)
        """

        tasks = self.repository.get_all(username)
        if task_name not in tasks:
            self.repository.add(username, task_name)

    def update_task(self, username, old_name, new_name):
        """Updates user repository with new task (housework)

        Args:
            username: Name of the user
            old_name: Name of the old housework, the housework which name user want's to get changed
            new_name: New name to the housework
        """

        tasks = self.repository.get_all(username)
        if old_name in tasks and new_name not in tasks:
            self.repository.update(username, old_name, new_name)

    def delete_task(self, username, task_name):
        """Deletes task (housework) from user's repository

        Args:
            username: Name of the user
            task_name: Name of the task (housework)
        """

        tasks = self.repository.get_all(username)
        if task_name in tasks:
            self.repository.delete(username, task_name)
