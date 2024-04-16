# Ohjelmistotekniikka, harjoitustyö

## Luetut kirjat -sovellus

**Sovelluksen** avulla _käyttäjä_ voi pitää kirjaa lukemistaan _kirjoista_ ja antaa niille _arvostelun_.

## Dokumentaatio

[Vaatimuusmäärittely](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/iita-mari/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)


## Asentaminen ##
1. Käytä riippuvuuksien asentamiseen komentoa _poetry install_
2. Aluksi pitää alustaa. Tee se komennolla _poetry run invoke build_
3. Sovelluksen käynnistämiseen käytä komentoa _poetry run invoke start_

## Muut komennot ##
* _poetry run invoke test_ -> testien suorittaminen
* _poetry run invoke coverage-report_ -> testikastavuusraportin koostaminen htmlcov-hakemistoon
* _poetry run invoke lint_ -> tee .pylintrc:iin määritellyt tarkistukset
