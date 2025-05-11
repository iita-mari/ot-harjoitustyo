from pathlib import Path
from repositories.housework_repository import HouseworkRepository
from repositories.contest_repository import ContestRepository
from services.housework_service import HouseworkService
from services.contest_service import ContestService

class AppView:
    """AppView is UI class for things happening after login.
    """

    def __init__(self, user):
        self.user = user
        self.housework_repository = HouseworkRepository()
        self.contest_repository = ContestRepository()
        self.housework_service = HouseworkService()
        self.contest_service = ContestService()

    def main(self):
        """Prints main menu of the app and leads different functions of the app

        Args:
            user_choice: User's choice
        """

        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print(f"Tervetuloa ~*{self.user.username}*~, olet kirjautunut Kotityö-sovellukseen")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print("")
        while True:
            print("Valitse toiminto: ")
            print("[1] Siirry Kotityö-kisaan")
            print("[2] Lisää/muokkaa/poista kotitöitä")
            print("[x] Kirjaudu ulos")
            print("")
            user_choice = input("Valinta: ")

            if user_choice == "1":
                self.contest()
            elif user_choice == "2":
                self.housework()
            elif user_choice == "x":
                print("")
                print("-----------------")
                print("Kirjaudutaan ulos")
                print("-----------------")
                return
            else:
                print("Virheellinen valinta.")

    def contest(self):
        """Prints Kotityö-competition -related things and asks which function user chooses

        Args:
            choice: User's choice
        """

        print("")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("Kotityö-kisa")
        print("Täällä voit katsoa Kotityö-kisan tilanteen sekä lisätä pisteitä kisataulukkoon")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("")
        tasks, grid = self.contest_service.get_contest_data(self.user.username)
        if not tasks:
            print("--------------------------------")
            print("Et ole vielä lisännyt kotitöitä.")
            print("--------------------------------")
            print("")
            return
        self._print_contest_grid(grid, tasks)

        print("")
        print("[1] Lisää piste")
        print("[2] Palaa edelliseen valikkoon")
        choice = input("Valinta: ")

        if choice == "1":
            self.add_point()
        elif choice == "2":
            self.main()

    def add_point(self):
        """ Add point(')s to user's housework-grid and shows points of the competition

        Args:
            row: houseworks lissted
            col: days form 1 to 31
            mark: nickname or other identifier for points
            grid: grid of the user's houseworks and points
        """

        tasks, grid = self.contest_service.get_contest_data(self.user.username)
        self._print_contest_grid(grid, tasks)
        print("")
        row = int(input(f"Valitse kotityörivin numero (ensimmäinen rivi - viimeinen rivi):1 - {len(tasks)}): ")) - 1
        col = int(input("Valitse päivän numero (1-31): ")) - 1
        mark = input("Syötä nimimerkki (esim. oma etukirjain): ")

        grid = self.contest_service.add_point(self.user.username, row, col, mark)
        print("")
        print("--------------")
        print("Piste lisätty!")
        print("--------------")


    def _print_contest_grid(self, grid, tasks):
        """Prints housework contest-grid

        Args:
            grid: grid with points
            tasks: housewoeks listed
        """

        task_col_width = max(len(f"{i+1}. {task}") for i, task in enumerate(tasks)) + 2
        print(" " * task_col_width + " ".join(f"{i+1:2}" for i in range(31)))
        print(" " * task_col_width + "-" * (3 * 31))

        for i, row in enumerate(grid):
            task_name = f"{i+1}. {tasks[i]}".ljust(task_col_width)
            row_content = " ".join(cell if cell else "." for cell in row)
            print(f"{task_name}{row_content}")

        mark_counts = self.contest_service.count_marks(grid)
        if mark_counts:
            print("")
            print("Pisteet:")
            for mark, count in sorted(mark_counts.items()):
                print(f"{mark}: {count}")


    def housework(self):
        """Menu, where user can list houseworks, add/edit/delete houseworks

        Args:
            user_choice: choice of user
        """


        print("")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("Lisää/muokkaa/poista kotitöitä")
        print("Täällä voit lisätä/muokata/poistaa kotitöitä")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("")

        while True:
            print("Valitse toiminto: ")
            print("[1] Lista Kotityö-kisan kotitöistä")
            print("[2] Lisää uusi kotityö")
            print("[3] Muokkaa olemassaolevaa kotityötä")
            print("[4] Poista olemassaoleva kotityö")
            print("[x] Palaa edelliseen valikkoon")
            print("")
            user_choice = input("Valitse toiminto: ")

            if user_choice == "1":
                tasks = self.housework_service.list_tasks(self.user.username)
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                    print("")
                if len(tasks) == 0:
                    print("--------------------------------")
                    print("VIRHE! Ei kotitöitä.")
                    print("Palataan edelliseen valikkoon...")
                    print("--------------------------------")
            elif user_choice == "2":
                print("")
                name = input("Kotityön nimi: ")
                self.housework_service.add_task(self.user.username, name)
                print("")
            elif user_choice == "3":
                print("")
                old = input("Kotityön vanha nimi: ")
                tasks = self.housework_service.list_tasks(self.user.username)

                if old not in tasks:
                    print("-----------------------------------------------")
                    print(f"VIRHE! Kotityötä '{old}' ei löytynyt listasta.")
                    print("-----------------------------------------------")
                    print("")
                    continue
                new = input("Uusi nimi: ")
                print("")
                self.housework_service.update_task(self.user.username, old, new)
            elif user_choice == "4":
                print("")
                name = input("Poistettavan kotityön nimi: ")
                tasks = self.housework_service.list_tasks(self.user.username)

                if name not in tasks:
                    print("")
                    print("-----------------------------------------------")
                    print(f"VIRHE! Kotityötä '{name}' ei löytynyt listasta.")
                    print("-----------------------------------------------")
                    print("")
                    continue
                self.housework_service.delete_task(self.user.username, name)
                print("")
            elif user_choice == "x":
                return
            else:
                print("----------------------------")
                print("VIRHE! Virheellinen valinta.")
                print("----------------------------")
