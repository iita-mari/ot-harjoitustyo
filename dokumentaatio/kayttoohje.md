# Käyttöohje

Lataa projektin tuorein releasen lähdekoodi: Assets-osio -> Source code.


## Ohjelman käynnistäminen
1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellus: `poetry run invoke start`

## Kirjautuminen
Sovellus käynnistuu sovelluksen alkunäkymään. Voit kirjautua sisään valitsemalla [1] ja painamalla Enter-näppäintä.

## Uuden käyttäjän luominen
Alkunäkymässä voit myös luoda uuden käyttäjän. Valitse silloin [2] ja paina Enter. Valitse ensin käyttäjänimi, jonka jälkeen salasana. Salasanan ja käyttäjätunnuksen tulee olla vähintään 4 merkkiä pitkiä. Kun olet luonut käyttäjän, palaat kirjautumisvalikkoon.

## Sovellusnäkymä
Kun olet kirjautunut sisään, toivotetaan sinut tervetulleeksi ja voit valita sovelluksen toimintoja. Valinta tehdään valitsemalla halutun toiminnon numero ja painamalla Enter-näppäintä.

[1] Siirry Kotityö-kisaan
- Täällä näet käyttäjän Kotityö-kisan tilanteen.
- Mikäli kotitöitä ja pisteitä on lisätty, näkyy myös pistetilanne tässä näkymässä.
- Mikäli kotitöitä on lisätty, näet täällä lisätyt kotityöt ja voit lisätä pisteitä kotitöiden tekemisestä.
  - Pisteitä lisätään valitsemalla tästä näkymästä [1] Lisää piste, jonka jälkeen:
    - Anna halutun kotityörivin numero
    - Anna päivän numero
    - Anna nimimerkki, joka on suorittanut kotityön
  - Voit myös valita edelliseen valikkoon valitsemalla [2]

[2] Lisää/muokkaa/poista kotitöitä
- Avaa valikon, jossa voit katsoa listan kisan kotitöistä, lisätä uuden kotityön, muokata olemassaolevaa kotityötä, poistaa olemassaolevan kotityön tai palata edelliseen valikkoon.
  - [1] Lista Kotityön-kisan kotitöistä: Listaa käyttäjän lisäämät kotityöt
  - [2] Kotityön lisäys: Voit lisätä kotitöitä listalle antamalla kotityön nimen.
  - [3] Kotityön muokkaus: Voit muokata listalla olevien kotitöiden nimiä. Anna ensin kotityön vanha nimi (kotityö, jonka nimeä haluat muokata), jonka jälkeen anna kotityölle uusi nimi.
  - [4] Kotityön poistaminen: Voit poistaa listalle lisätyn kotityön antamalla poistettavan kotityön nimen.
  - [x ] Palaa edelliseen valikkoon

[x] Kirjaudu ulos
- Kirjaa käyttäjän ulos ja siirtyy kirjautumisnäkymään.
