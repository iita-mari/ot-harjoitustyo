from pathlib import Path
from repositories.housework_repository import HouseworkRepository
from repositories.contest_repository import ContestRepository
from services.housework_service import HouseworkService
from services.contest_service import ContestService

class AppView:
    def __init__(self, user):
        self.user = user
        self.housework_repository = HouseworkRepository()
        self.contest_repository = ContestRepository()
        self.housework_service = HouseworkService()
        self.contest_service = ContestService()

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
                print("Valitsit 'Kirjaudu ulos'. Kirjaudutaan ulos.")
                #tässä bugi, miten pääsen kirjautumaan ulos?
                break
            else:
                print("Virheellinen valinta.")

    def contest(self):
        print("Kotityö-kisa")
        print("Täällä voit katsoa Kotityö-kisan tilanteen sekä lisätä pisteitä kisataulukkoon")
        tasks, grid = self.contest_service.get_contest_data(self.user.username)
        if not tasks:
            print("Et ole vielä lisännyt kotitöitä.")
            return
        self._print_contest_grid(grid, tasks)

        print("\n[1] Lisää piste")
        print("[2] Palaa valikkoon")
        choice = input("Valinta: ")

        if choice == "1":
            self.add_point()
        elif choice == "2":
            self.main()

    def add_point(self):
        tasks, grid = self.contest_service.get_contest_data(self.user.username)
        self._print_contest_grid(grid, tasks)
        row = int(input(f"Valitse rivin numero (1-{len(tasks)}): ")) - 1
        col = int(input("Valitse päivän numero (1-31): ")) - 1
        mark = input("Syötä merkki (esim. oma etukirjain): ")

        grid = self.contest_service.add_point(self.user.username, row, col, mark)
        print("Piste lisätty!")


    def _print_contest_grid(self, grid, tasks):
        task_col_width = max(len(task) for task in tasks) + 2
        print(" " * task_col_width + " ".join(f"{i+1:2}" for i in range(31)))
        print(" " * task_col_width + "-" * (3 * 31))

        for i, row in enumerate(grid):
            task_name = tasks[i].ljust(task_col_width)
            row_content = " ".join(cell if cell else "." for cell in row)
            print(f"{task_name}{row_content}")

        mark_counts = self.contest_service.count_marks(grid)
        if mark_counts:
            print("\nPisteet:")
            for mark, count in sorted(mark_counts.items()):
                print(f"{mark}: {count}")


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
                tasks = self.housework_service.list_tasks(self.user.username)
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            elif user_choice == "2":
                name = input("Kotityön nimi: ")
                self.housework_service.add_task(self.user.username, name)
            elif user_choice == "3":
                old = input("Kotityön vanha nimi: ")
                new = input("Uusi nimi: ")
                self.housework_service.update_task(self.user.username, old, new)
            elif user_choice == "4":
                name = input("Poistettavan kotityön nimi: ")
                self.housework_service.delete_task(self.user.username, name)
            elif user_choice == "5":
                self.main()
            else:
                print("Virheellinen valinta.")
