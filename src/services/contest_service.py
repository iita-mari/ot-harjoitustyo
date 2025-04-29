from repositories.contest_repository import ContestRepository
from repositories.housework_repository import HouseworkRepository

class ContestService:
    def __init__(self):
        self.contest_repository = ContestRepository()
        self.housework_repository = HouseworkRepository()

    def get_contest_data(self, username):
        tasks = self.housework_repository.get_all(username)
        grid = self.contest_repository.load_grid(username, len(tasks))
        return tasks, grid

    def add_point(self, username, row_index, col_index, mark):
        tasks = self.housework_repository.get_all(username)
        grid = self.contest_repository.load_grid(username, len(tasks))
        grid[row_index][col_index] = mark
        self.contest_repository.save_grid(username, grid)
        return grid

    def count_marks(self, grid):
        all_marks = [cell for row in grid for cell in row if cell]
        return {mark: all_marks.count(mark) for mark in set(all_marks)}
