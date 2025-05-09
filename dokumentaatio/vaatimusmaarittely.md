# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovelluksen tarkoituksena on mahdollistaa kotitöiden listaus ja niiden tekemisessä kisailu. Sovelluksessa kotitaloudelle voidaan määrittää listaus kotitöistä. Kotitöitä voidaan merkata tunnistettavasti eri kotitalouden jäsenten tekemäksi (eri värit/nimet/tms.). Sovellus pitää kirjaa, kuka kotitalouden jäsen on tehnyt eniten kotitöitä. Sovellukseen on mahdollista rekisteröityä useampi eri kotitalous, joilla jokaisella on oma listaus kotitöistä ja omat kotitalouden jäsenet.

## Käyttäjät
Alussa käyttäjiä on vain yksi käyttäjärooli, joka kuvastaa yhtä _kotitaloutta_ ja on ns. _normaali käyttäjä_. Myöhemmin on mahdollista, että käyttäjärooleja on kaksi, jolloin käyttäjät jakaantuvat _kotitalouden jäseniin_ ja _kotitalouteen_. Sovelluksen edetessä saatetaan lisätä myös _pääkäyttäjän_ rooli sovellukseen.

## Suunnitellut toiminnallisuudet perusversiossa


### Aloitus ja kirjautuminen
- TEHTY: Sovellukseen voi luoda kotitalouden eli käyttäjän. (Eli yhdellä kotitaloudella on yksi käyttäjä/-tunnus).
  - TEHTY: Käyttäjätunnus on uniikki ja vähintään 4 merkkiä pitkä
  - TEHTY: Salasana on vähintään 4 merkkiä pitkä
 - TEHTY: Sovellukseen voi kirjautua
   - TEHTY: Oikea, rekisteröity käyttäjätunnus yhdessä oikean salasanan kanssa kirjaavat kotitalouden/käyttäjän sisään sovellukseen
   - TEHTY: Väärästä tunnuksesta tai salasanasta tulee virheviesti
   - TEHTY: Mikäli kotitaloutta/käyttäjää ei ole olemassa, ilmoitetaan tästä virheviestillä

### Kirjautumisen jälkeen eli sovellusnäkymä
- TEHTY: Kotitalous/käyttäjä näkee listauksen kotitöistä
  - TEHTY: Näkymä on karkea "excelmäinen kuukausinäkymä" (kts. [alkuperäinen paperiversio, kotityö-kilpailu](https://www.instagram.com/p/C9SZ7isNEEx/))
  - TEHTY: Kotitöitä voi merkata eri kotitalouden jäsenten tekemiksi
- TEHTY: Kotitöitä voi lisätä, muokata ja poistaa
- Kotitalouden jäseniä voi lisätä, muokata ja poistaa
- TEHTY: Sovellus kertoo, kuka on johdolla tehdyissä kotitöistä eli kenelle kotitalouden jäsenelle on merkattu eniten kotitöitä tehdyiksi
- TEHTY: Sovelluksesta voi kirjautua ulos

## Jatkokehitysideat
- Myöhemmässä vaiheessa eri kotitöille voidaan määrittää erilaiset pistearvot
- Kotitöitä voidaan määrittää päivittäin/viikottain/kuukausittain tehtäväksi. Tällöin kotityöstä saadut pisteet saa vain kerran päivässä/viikossa/kuukaudessa
- Sovelluksessa on kotitöille päivä-, viikko- ja kuukausinäkymät, joita voi vaihdella
- Kotitalous ja kotitalouden jäsenet eriytetään, jolloin kotitalouden jäsenet liittyvät tiettyyn kotitaloudeen koodilla tai vastaavalla tunnisteella.
    - Tällöin kotitalouden jäsen voi merkata vain itselleen pisteitä ja liittyä tarvittaessa useampaan kotitalouteen.
- Kotitalouden johdossa oleva jäsen on jollain tavalla korostettuna visuaalisesti sovelluksessa
- Sovelluksessa on viikottaiset/kuukausittaiset/vuosittaiset tilastot kerätyistä pisteistä kotitalouskohtaisesti
  - Yksittäisellä kotitalouden jäsenellä on omat tilastonsa, joissa näkyy tehdyt kotityöt viikoittain/kuukausittain/vuosittain
