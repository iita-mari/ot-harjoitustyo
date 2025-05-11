# Changelog

## Viikko 3

- (Teksti)käyttöliittymän runko hahmoteltu
- Kirjautuminen ja uuden käyttäjän luominen aluillaan
- Ensimmäinen testi tehty

## Viikko 4
- Uuden käyttäjän luominen onnistuu
  - UserRepository tehty
    - Kirjautumistiedot tallennetaan .csv-tiedostoon
- Kirjautuminen tarkistetaan: käyttäjätietojen tulee olla luotu
- Kirjautuneena pääsee sovellus-näkymään (app_view)
- Sovellusnäkymä (app_view) aloitettu
- Testaus: alustavaa hahmotelmaa UserRepositoryn testaamisesta, ei toimi vielä

## Viikko 5
- App_view näyttää kotityökisan kisataulukon
- Kisaan voi lisätä kotitöitä
- Kisataulukkoa voi täyttää
- Kotitöitä voi luoda, muokata ja poistaa
- Kisataulukko ja kotityöt tallennetaan .csv-tiedostoon
- Testaus: UserRepositoryyn ja HouseworkRepositoryyn testejä

## Viikko 6
- Erotettu services-luokkia ui:sta
- Nyt käyttäjätunnuksen tulee olla uniikki ja vähintään 4 merkkiä pitkä
- Nyt väärästä tunnuksesta (olemassa oleva tai liian lyhyt) tai väärästä salasanasta tulee virheviesti
- Testaus: Muutama testi lisää repositoryyn ja aloitettu service-luokkiin testien kirjoittaminen

## Viikko 7
- Siistitty ja paranneltu käyttöliittymää
- Korjattu bugeja ja lisätty virheviestejä
- Jatkettu Docstringien parissa
- Päivitetty sovelluksen dokumentaatiota, mm. käyttöohjetta
