import csv
from pathlib import Path
from repositories.housework_repository import HouseworkRepository
from repositories.contest_repository import ContestRepository

class AppView:
    def __init__(self, user):
        self.user = user
        self.housework_repo = HouseworkRepository()
        self.contest_repo = ContestRepository()

    def main(self):
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print(f"Tervetuloa, {self.user.username}, olet kirjautunut Kotityö-sovellukseen")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("")
        while True:
            print("Valitse toiminto: ")
            print("[1] Siirry Kotityö-kisaan")
            print("[2] Lisää/muokkaa/poista kotitöitä")
            print("[3] Kirjaudu ulos")
            user_choice = input("Valitse toiminto: ")

            if user_choice == "1":
                self.contest()
            elif user_choice == "2":
                self.housework()
            elif user_choice == "3":
                print("Valitsit 'Kirjaudu ulos'. Palaat aloitusvalikkoon.")
                break
            else:
                print("Virheellinen valinta.")

    def contest(self):
        print("Kotityö-kisa")
        print("Täällä voit katsoa Kotityö-kisan tilanteen sekä lisätä pisteitä kisataulukkoon")
        tasks = self.housework_repo.get_all(self.user.username)
        if not tasks:
            print("Et ole vielä lisännyt kotitöitä.")
            return
        else:
            grid = self.contest_repo.load_grid(self.user.username, len(tasks))
            self._print_contest_grid(grid, tasks)

        print("\n[1] Lisää piste")
        print("[2] Palaa valikkoon")
        choice = input("Valinta: ")

        if choice == "1":
            self.add_point()
        elif choice == "2":
            self.main()

    def add_point(self):
        tasks = self.housework_repo.get_all(self.user.username)
        grid = self.contest_repo.load_grid(self.user.username, len(tasks))
        self._print_contest_grid(grid, tasks)
        tasks = self.housework_repo.get_all(self.user.username)
        row = int(input("Valitse rivin numero (1-[]): ".format(len(tasks)))) - 1
        col = int(input("Valitse päivän numero (1-31): ")) - 1
        mark = input("Syötä merkki (esim. oma etukirjain): ")

        grid[row][col] = mark
        self.contest_repo.save_grid(self.user.username, grid)
        print("Piste lisätty!")


    def _print_contest_grid(self, grid, tasks):
        task_col_width = max(len(task) for task in tasks) + 2

        print(" " * task_col_width + " ".join(f"{i+1:2}" for i in range(31)))
        print(" " * task_col_width + "-" * (3 * 31))

        for i, row in enumerate(grid):
            task_name = tasks[i].ljust(task_col_width)
            row_content = " ".join(cell if cell else "." for cell in row)
            print(f"{task_name}{row_content}")

        all_marks = [cell for row in grid for cell in row if cell]
        if all_marks:
            print("\nPisteet:")
            for mark in sorted(set(all_marks)):
                print(f"{mark}: {all_marks.count(mark)}")


    def housework(self):
        print("Lisää/muokkaa/poista kotitöitä")
        print("Täällä voit lisätä/muokata/poistaa kotitöitä")

        while True:
            print("Valitse toiminto: ")
            print("[1] Lista Kotityö-kisan kotitöistä")
            print("[2] Lisää uusi kotityö")
            print("[3] Muokkaa olemassaolevaa kotityötä")
            print("[4] Poista olemassaoleva kotityö")
            print("[5] Palaa päävalikkoon")
            user_choice = input("Valitse toiminto: ")

            if user_choice == "1":
                tasks = self.housework_repo.get_all(self.user.username)
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            elif user_choice == "2":
                name = input("Kotityön nimi: ")
                self.housework_repo.add(self.user.username, name)
            elif user_choice == "3":
                old = input("Kotityön vanha nimi: ")
                new = input("Uusi nimi: ")
                self.housework_repo.update(self.user.username, old, new)
            elif user_choice == "4":
                name = input("Poistettavan kotityön nimi: ")
                self.housework_repo.delete(self.user.username, name)
            elif user_choice == "5":
                self.main()
            else:
                print("Virheellinen valinta.")
