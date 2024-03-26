# Vaatimusmäärittely #

## Sovelluksen tarkoitus ##
Sovelluksella käyttäjä voi pitää kirjaa kirjoista, jotka käyttäjä on lukenut. Sovelluksessa kirjoja voi arvostella.

## Käyttäjä/t ##
Käyttäjärooleja on alkuun vain yksi, esimerkiksi *lukija*. Sovelluksen edistyessä voidaan lisätä tarvittaessa myös lisää erilaisia käyttäjäryhmiä, kuten *pääkäyttäjä*.

## Suunnitelut toiminnallisuudet
#### Ennen kirjautumista ####
* Käyttäjä voi luoda uuden käyttäjätunnuksen
	* Käyttäjä voi itse määritellä käyttäjätunnuksensa
	* Käyttäjä voi itse määritellä salasanan
* Käyttäjä voi kirjautua sisään käyttäjätunnuksella ja salasanalla
	* Jos käyttäjätunnus ja salasana täsmäävät olemassa olevaan käyttäjään, kirjaudutaan sisään
	* Jos käyttäjää ei ole, tästä tulee ilmoitus
	* Jos kirjautumistiedoista jompi kumpi on väärin, tästä tulee ilmoitus
 
#### Kirjautumisen jälkeen ####
* Käyttäjä voi kirjata sovellukseen lukemansa kirjan
	* Käyttäjä syöttää kirjalle tekijän
	* Käyttäjä syöttää kirjan nimen
	* Käyttäjä syöttää kirjan arvostelun asteikolla 1-5
* Käyttäjän on mahdollista nähdä listaus lukemistaan kirjoista

## Jatkokehitysideat
Perusversiota voidaan täydentää mahdollisesti esimerkiksi seuraavilla toiminnallisuuksilla:
* Luetuille kirjoille tai kirjaryhmille voi määritellä värin
	* Väri toistuu esimerkiksi arvostelun mukaan
* Arvosteluasteikko on visuaalinen
	* Käyttäjä voi esimerkiksi valita sopivan tähtimäärän (1-5 tähteä)
* Luettuihin kirjoihin voi merkata, pitikö kirjoittajasta
	*  Sovelluksessa on erikseen sivu, joka listaa kirjoittajat joista käyttäjä on pitänyt
* Sovelluksessa on käyttäjäryhmiä
	* Yksittäinen käyttäjä voi liittyä käyttäjäryhmään
	* Käyttäjäryhmän käyttäjät näkevät toistensa lukemat kirjat ja niiden arvostelut
	* Halutessaan käyttäjä voi valita, näytetäänkö sovellukseen syötetty kirja käyttäjäryhmälle vai vain hänelle itselleen    
