import os
from repositories.user_repository import UserRepository, User
from ui.app_view import AppView
from services.user_service import UserService

dirname = os.path.dirname(__file__)
user_file_path = os.path.join(dirname, "..", "data", "users.csv")
user_repository = UserRepository(user_file_path)
user_service = UserService(user_repository)


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

        user = user_service.authenticate(username, password)

        if user:
            print("Kirjautuminen onnistui!")
            AppView(user).main()
        else:
            existing_user = user_repository.find_by_username(username)

            if not existing_user:
                print("Käyttäjätunnusta ei ole olemassa.")
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
            if len(username) < 4:
                print("Käyttäjätunnuksen pitää olla vähintään 4 merkkiä.")
                break
            password = input("Anna salasana: ")
            if len(password) < 4:
                print("Salasanan tulee olla vähintään 4 merkkiä.")
                break
            password2 = input("Anna salasana uudestaan: ")

            result = user_service.create_user(username, password, password2)

            if result is True:
                print("Käyttäjätunnus on jo käytössä.")
            elif result is False:
                print("Salasanat eivät olleet samat!")
            else:
                print("Käyttäjä luotu!")
                break

    def exit_login(self):
        print("Valitsit 'poistu'. Kiitos ja näkemiin!")
