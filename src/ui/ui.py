import os
from repositories.user_repository import UserRepository, User
from ui.app_view import AppView

dirname = os.path.dirname(__file__)
user_file_path = os.path.join(dirname, "..", "data", "users.csv")
user_repository = UserRepository(user_file_path)


class UI:
    def __init__(self):
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("* Tervetuloa Kotityö-sovellukseen *")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

    def start(self):
        print("")
        while True:
            print("Valitse toiminto:")
            print("[1] Kirjaudu sisään")
            print("[2] Luo uusi käyttäjä")
            print("[x] Poistu")
            print("")

            user_choice = input("Valinta: ")

            if user_choice == "1":
                self.user_login()
            elif user_choice == "2":
                self.new_user()
            elif user_choice.lower() == "x":
                self.exit_login()
                break
            else:
                print("Virheellinen valinta!")

    def user_login(self):
        print("-----------------------")
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        print("")

        user = user_repository.find_by_username(username)

        if user and user.password == password:
            print("Kirjautuminen onnistui!")
            AppView(user).main()

        else:
            print("Väärä käyttäjätunnus tai salasana.")
            print("")
            print("Kokeile uudestaan?")
            print("[1] Kyllä")
            print("[2] Ei")
            user_choice = input("Valinta: ")

            if user_choice == "1":
                self.user_login()
            elif user_choice == "2":
                print("Kiitos ja näkemiin! Palaat aloitusvalikkoon")
                self.start()

    def new_user(self):
        print("-----------------------")
        while True:
            username = input("Anna käyttäjätunnus: ")
            if user_repository.find_by_username(username):
                print("Käyttäjätunnus on jo käytössä.")
                continue

            password = input("Anna salasana: ")
            password2 = input("Anna salasana uudestaan: ")

            if password != password2:
                print("Salasanat eivät olleet samat!")
                continue

            user_repository.create(User(username, password))
            print("-----------------------")
            break

    def exit_login(self):
        print("Valitsit 'poistu'. Kiitos ja näkemiin!")
