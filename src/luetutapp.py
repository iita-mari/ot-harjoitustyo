class Ui:

    def __init__(self):
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
        print("* Tervetuloa Luetut kirjat-appiin *")
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
        read_books_view()


    def new_user(self):
        while True:
            new_username = input("Anna käyttäjätunnus: ")
            new_password = input("Anna salasana: ")
            new_password_again = input("Anna salasana uudestaan: ")

            if new_password != new_password_again:
                print("Salasanat eivät olleet samat!")
                continue
            print("Käyttäjän luonti onnistui!")
            booklist[new_username] = []
            print("")
            break

    def exit_login(self):
        print("Kiitos ja näkemiin!")


    def read_books_view(self, user_name):
        print("Tervetuloa!")
        print("Olet lukenut seuraavat kirjat:")
        list_of_books()
        

    def list_of_books(self, user_name):
        return self.booklist.get(user_name)

    def add_book(self, user_name, book_name, rating):
        if user_name in self.booklist:
            self.booklist[user_name].append({"book": book_name, "rating": rating})
            print(f"Kirja '{book_name}' lisätty {user_name}! Arvostelusi kirjalle: {rating}!")
        else:
            print("Käyttäjätunnusta ei löydy!")





ui = Ui()
ui.start()
