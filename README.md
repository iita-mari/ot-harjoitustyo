# Ohjelmistotekniikka, harjoitustyö

## Kotityö-sovellus
Sovelluksen avulla kotitalouden jäsenet voivat merkata listattuja kotitöitä tehdyksi. Kotityön tekemisestä saa *pisteen*, ja kuun lopuksi eniten *pisteitä* saanut on **voittaja**. Sovellus perustuu [kotityö-kilpailuun, jonka Gogi Mavromichalis on esitellyt Instagramissa](https://www.instagram.com/p/C9SZ7isNEEx/).

**HUOM!** Käytäthän vähintään Python-versiota 3.10

## Dokumentaatio
- [Vaatimusmäärittely](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [Työaikakirjanpito](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [Changelog](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus
1. Asenna riippuvuudet: `poetry install`
2. Käynnistä sovellut: `poetry run invoke start`

## Kontorivitoiminnot
- Suorita ohjelma: `poetry invoke start`
- Suorita testit: `poetry run invoke test`
- Generoi testikattavuusraportti htmlcov-hakemistoon: `poetry run invoke coverage-report`
