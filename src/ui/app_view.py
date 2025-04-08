class AppView:
    def __init__(self, user):
        self.user = user

    def main(self):

        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*")
        print(
            f"* Tervetuloa, {self.user.username}, olet kirjautunut Kotityö-sovellukseen *")
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
        print(
            "Täällä voit katsoa Kotityö-kisan tilanteen sekä lisätä pisteitä kisataulukkoon")

    def housework(self):
        print("Lisää/muokkaa/poista kotitöitä")
        print("Täällä voit lisätä/muokata/poistaa kotitöitä")

        while True:
            print("Valitse toiminto: ")
            print("[1] Lista kotityö-kisan kotitöistä")
            print("[2] Lisää uusi kotityö")
            print("[3] Muokkaa olemassaolevaa kotityötä")
            print("[4] Poista olemassaoleva kotityö")
