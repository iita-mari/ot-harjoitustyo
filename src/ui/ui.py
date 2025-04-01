class UI:
    def __init__(self):
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("* Tervetuloa Kotityö-sovellukseen *")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("")
    
    def start(self):
        while True:
            print("Valitse toiminto:")
            print("[1] Kirjaudu sisään")
            print("[2] Luo uusi käyttäjä")
            print("[x] Poistu")
            print("")

            user_choice = input("")

            if user_choice == "1":
                self.user_login()
            elif user_choice == "2":
                self.new_user()
            elif user_choice.lower() == "x":
                self.exit_login()
                break

    def user_login(self):
        user_name = input("Anna käyttäjätunnus: ")
        password = input("Anna salasana: ")

        print("Kirjautuminen onnistui!")
        print("")
        # siirtyminen sovellus-näkymään


    def new_user(self):
        while True:
            new_username = input("Anna käyttäjätunnus: ")
            new_password = input("Anna salasana: ")
            new_password_again = input("Anna salasana uudestaan: ")

            if new_password != new_password_again:
                print("Salasanat eivät olleet samat!")
                continue
            print("Käyttäjän luonti onnistui!")
            # siirtyminen kirjautuminen-näkymään
            print("")
            break

    def exit_login(self):
        print("Kiitos ja näkemiin!")
        return "Kiitos ja näkemiin!"