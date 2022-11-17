class Opintoseuranta:

    kayttajatunnus = "nakki"
    salasana = "muusi"

    minne = int (input("1. vie kirjautumaan: "))
    if minne == 1:
        kayttajatunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")

        if kayttajatunnus == "nakki":
            if salasana == "muusi":
                print("Kirjautuminen onnistui!")
        else:
            print("Väärin meni!")


