# Vaatimuusmäärittely #

## Sovelluksen tarkoitus ##

Sovelluksen avulla käyttäjät pystyvät pitämään kirjaa kurssitehtävistään. Jokaisella käyttäjällä on oma tehtävälista, jonka pääsee näkemään vain kirjatumalla omalle käyttäjälleen.

Sovellus kysyy kurssitehtävän pistemäärän ja laskee kuinka monta prosenttia pisteet ovat suhteessa kurssin kokonaispistemääräästä. Pistemäärien (tehtävä ja kurssin kokonaispistemäärä) avulla sovellus myös antaa käyttäjälle arvioin, kuinka paljon laskennallisesti kurssitehtävään on hyvä varata aikaa. Ajan laskemisessa hyödynnetään kurssin opintopistemäärää (1 op = 27 h), kurssin kokonaispistemäärää ja tehtäväpistemäärää.

## Käyttäjä/t ##
Käyttäjärooleja on alkuun vain yksi, esimerkiksi *opiskelija*. Sovelluksen edistyessä voidaan lisätä tarvittaessa myös lisää erilaisia käyttäjäryhmiä, jotka voisivat olla esimerkiksi *pääkäyttäjä* ja *opettaja*.


## Suunnitellut toiminnallisuudet ##
#### Ennen kirjautumista ####
* Käyttäjä voi kirjautua sisään käyttäjätunnuksella ja salasanalla
    * Jos käyttäjätunnus ja salasana täsmäävät olemassa olevaan käyttäjään, kirjaudutaan sisään
    * Jos käyttäjää ei ole, tästä tulee ilmoitus
    * Jos kirjautumistiedoista jompi kumpi on väärin, tästä tulee ilmoitus
* Käyttäjä voi luoda uuden käyttäjätunnuksen
	* Salanana tulee syöttää kahdesti ja syötettyjen salasanojen tulee täsmätä toisiaan
	* Jos salasanat eivät tästää, tästä tulee ilmoitus
	* Jos salasanat täsmäävät, luodaan uusi käyttäjä ja siirrytään kirjautumisnäkymään

#### Kirjautumisen jälkeen ###
* Käyttäjä näkee listauksen tulevista, tekemättömista kurssitehtävistä
	* Mahdollisesti aikajärjestyksessä, järjestettynä lähimmän deadlinen mukaan
* Käyttäjä voi merkata tehtävän tehdyksi
	* Kurssitehtävä katoaa listalta
* Käyttäjä voi kirjata (tai siirtyä kirjaamaan uudessa näkymässä) uuden kurssitehtävän
* Käyttäjä voi kirjautua ulos tunnukseltaan
	* Kirjautuminen ulos vie näkymään, jossa voi kirjautua takaisin sovellukseen

### Uuden kurssitehtävän kirjaaminen ###
* Käyttäjä voi kirjata uuden kurssitehtävän
	* Kurssitehtävälle voidaan antaa seuraavia tietoja:
	    * Tehtävän nimi / tunniste
		* Tehtävän pistemäärä
		* Tehtävän deadline
        * Kurssin nimi / tunniste, jolle tehtävä kuuluu
		    * Kurssin opintopistemäärä, mikäli kurssia ei ole kirjattu aiemmin
		    * Kurssin kokonaispistemäärä, mikäli kurssia ei ole kirjattu aiemmin


## Jatkokehitysideoita ##
Perusversiota voidaan täydentää mahdollisesti esimerkiksi seuraavilla toiminnallisuuksilla:
* Tehty tehtävä siirtyy omaan listaukseensa
* Kurssille voi määritellä värin
	* Väri toistuu kaikissa saman kurssin tehtävissä
	* Väri muuttuu, kun tehtävä on tehty / siirtyy tehtyjen listalle
* Tekemättömiin tehtäviin tulee jonkinlainen ikoni tai värimuutos, mikäli deadline on lähellä
	* Omat värit esim. Jos deadline 5 päivän sisällä, jos deadline 3 päivän sisällä
* Listauksessa näkyy myös kurssin suorituksen edistyminen, esimerkiksi prosenttimääränä tai edistymispalkkina
* Tehtävälle voi laskea, kuika paljon siihen kannattaa varata aikaa ilman, että syöttää tehtävän tehtävälistaan
