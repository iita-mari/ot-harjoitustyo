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
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("Tervetuloa Kotityö-sovellukseen")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

    def start(self):
        while True:
            print("")
            print("~*~*~*~*~*~*~*~*~*~")
            print("Kirjautumisvalikko")
            print("~*~*~*~*~*~*~*~*~*~")
            print("")
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
                print("")
                print("---------------------------")
                print("VIRHE! Virheellinen valinta!")
                print("---------------------------")

    def user_login(self):
        print("")
        print("~*~*~*~*~*~*~*~*~")
        print("Kirjaudu sisään")
        print("~*~*~*~*~*~*~*~*~")
        print("")
        username = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")
        print("")

        user = user_service.authenticate(username, password)

        if user:
            print("-----------------------")
            print("Kirjautuminen onnistui!")
            print("Siirryt sovellukseen...")
            print("-----------------------")
            print("")
            AppView(user).main()
        else:
            existing_user = user_repository.find_by_username(username)

            if not existing_user:
                print("----------------------------------------")
                print("VIRHE! Käyttäjätunnusta ei ole olemassa.")
                print("Palataan edelliseen valikkoon...")
                print("----------------------------------------")
            else:
                print("-----------------------------------------")
                print("VIRHE! Väärä käyttäjätunnus tai salasana.")
                print("Yritä uudestaan?")
                print("-----------------------------------------")
                print("[1] Kyllä")
                print("[2] Ei")
                print("")
                user_choice = input("Valinta: ")

                if user_choice == "1":
                    self.user_login()
                elif user_choice == "2":
                    print("---------------------")
                    print("Palataan edelliseen valikkoon...")
                    print("---------------------")
                    self.start()
                else:
                    print("---------------------------")
                    print("VIRHE!Virheellinen valinta!")
                    print("---------------------------")


    def new_user(self):
        print("")
        print("~*~*~*~*~*~*~*~*~*~")
        print("Luo uusi käyttäjä")
        print("~*~*~*~*~*~*~*~*~*~")
        print("")
        while True:
            username = input("Anna käyttäjätunnus (vähintään 4 merkkiä): ")
            if len(username) < 4:
                print("")
                print("---------------------------------------------------------")
                print("VIRHE! Käyttäjätunnuksen pitää olla vähintään 4 merkkiä.")
                print("Palataan valikkoon...")
                print("---------------------------------------------------------")
                print("")
                break
            password = input("Anna salasana (vähintään 4 merkkiä): ")
            if len(password) < 4:
                print("")
                print("---------------------------------------------------")
                print("VIRHE! Salasanan tulee olla vähintään 4 merkkiä.")
                print("Palataan valikkoon...")
                print("---------------------------------------------------")
                print("")
                break
            password2 = input("Anna salasana uudestaan: ")
            print("")

            result = user_service.create_user(username, password, password2)

            if result == "username_taken":
                print("--------------------------------------")
                print("VIRHE! Käyttäjätunnus on jo käytössä.")
                print("Kokeile uudestaan:")
                print("--------------------------------------")
                print("")
            elif result == "passwords_dont_match":
                print("--------------------------------------")
                print("VIRHE! Salasanat eivät olleet samat!")
                print("Kokeile uudestaan:")
                print("--------------------------------------")
                print("")
            elif result == "success":
                print("-------------------------")
                print("Käyttäjä luotu!")
                print("Palataan valikkoon...")
                print("-------------------------")
                print("")
                break

    def exit_login(self):
        print("")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("Sovellus suljetaan. Kiitos ja näkemiin!")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
