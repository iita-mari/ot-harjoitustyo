class Ui:

    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("Tervetuloa opintoseuranta-appiin")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("")

    while (True):
        print("Valitse toiminto:")
        print("[1] Kirjaudu sisään")
        print("[2] Luo uusi käyttäjä")
        print("[x] Poistu")
        print("")

        user_choice = input("")

        if user_choice == "1":
            user_name = input("Anna käyttäjätunnus: ")
            password = input("Anna salasana: ")
            print("")

        elif user_choice == "2":
            while True:
                new_username = input("Anna käyttäjätunnus: ")
                new_password = input("Anna salasana: ")
                new_password_again = input("Anna salasana uudestaan: ")

                if new_password != new_password_again:
                    print("Salasanat eivät olleet samat!")
                    continue
                elif new_password == new_password_again:
                    print("Käyttäjän luonti onnistui!")
                    print("")
                    break
            continue
        elif user_choice== "x" or "X":
            print("Kiitos ja näkemiin!")
            break