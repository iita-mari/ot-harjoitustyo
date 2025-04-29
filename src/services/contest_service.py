from repositories.contest_repository import ContestRepository
from repositories.housework_repository import HouseworkRepository

class ContestService:
    """Service class for housework-contest related things.
    """

    def __init__(self):
        self.contest_repository = ContestRepository()
        self.housework_repository = HouseworkRepository()

    def get_contest_data(self, username):
        """Get contest data of user

        Args:
            username: Name of the user

        Returns:
            tasks: User's houseworks
            grid: Grid for user's houseworks
        """

        tasks = self.housework_repository.get_all(username)
        grid = self.contest_repository.load_grid(username, len(tasks))
        return tasks, grid

    def add_point(self, username, row_index, col_index, mark):
        """Add point to user's housework grid

        Args:
            username: User's username
            row_index: Row of the housework
            col_index: Column of the day
            mark: Marks point to grid

        Returns:
            grid: Returns grid, where point is marked
        """

        tasks = self.housework_repository.get_all(username)
        grid = self.contest_repository.load_grid(username, len(tasks))
        grid[row_index][col_index] = mark
        self.contest_repository.save_grid(username, grid)
        return grid

    def count_marks(self, grid):
        """Counts marks in user's grid

        Args:
            grid: user's housework grid

        Returns:
            count of marks: count's marks and returns amount of them 
        """

        all_marks = [cell for row in grid for cell in row if cell]
        return {mark: all_marks.count(mark) for mark in set(all_marks)}
