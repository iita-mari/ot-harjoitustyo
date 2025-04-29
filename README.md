# Ohjelmistotekniikka, harjoitustyö

## Kotityö-sovellus
Sovelluksen avulla kotitalouden jäsenet voivat merkata listattuja kotitöitä tehdyksi. Kotityön tekemisestä saa *pisteen*, ja kuun lopuksi eniten *pisteitä* saanut on **voittaja**. Sovellus perustuu [kotityö-kilpailuun, jonka Gogi Mavromichalis on esitellyt Instagramissa](https://www.instagram.com/p/C9SZ7isNEEx/).

**HUOM!** Käytäthän vähintään Python-versiota 3.10 sovelluksen kanssa.

## Release
- [Viikko 5:n release](https://github.com/iita-mari/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
- [Käyttöohje](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

- [Vaatimusmäärittely](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/iita-mari/ot-harjoitustyo/blob/997a43c548e2ee792bea6e17b5692596838a7344/dokumentaatio/arkkitehtuuri.md) 

- [Työaikakirjanpito](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus
1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellus: `poetry run invoke start`

## Komentorivitoiminnot
- Suorita ohjelma: `poetry invoke start`
- Suorita testit: `poetry run invoke test`
- Generoi testikattavuusraportti htmlcov-hakemistoon: `poetry run invoke coverage-report`
- Tarkistus *.pylintrc*-tiedoston mukaisesti: `poetry run invoke lint`
