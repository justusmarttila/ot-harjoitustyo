# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen tarkoitus on kehittää käyttäjän matemaattista hahmotuskykyä ja tuottaa mielihyvää pelaamalla Miinaharavaa.
Monet ovat kertoneet, että pelit ovat auttaneet rentoutumaan ja ottamaan ajatukset irti stressaavasta arjesta.
## Käyttäjät
Yksi käyttäjä, lisäksi tulokset tallennetaan highscore tauluun, joten pelin voi viedä webiin ja käyttäjät voivat kilpailla toisiaan vastaan.
## Toiminnallisuudet
### Ennen kirjautumista
* Käyttäjät voi luoda tunnuksen, johon liitetään käyttäjän pelaamien pelien ajat
    * Käyttäjätunnuksen tulee olla vähintään 4 merkkiä ja uniikki
* Tunnuksien avulla voidaan kirjuatua, jos tunnuksia ei ole ehdotetaan tunnuksien luomista
### Kirjautumisen jälkeen
* Käyttäjä valitsee joko beginner, intermediate, expert tai päättää itse ruudukon koon ja miinojen määrän (tehty)
    * Beginner on 9x9 10 miinalla, intermediate on 16x16 40 miinalla ja expert on 16x30 99 miinalla
* Valinnan jälkeen generoidaan valittu muoto (tehty)
* miinoja pystyy merkkaamaan ja laattoja pystyy avaamaan (tehty)
* miinan avaamisesta häviää pelin ja kaikkien numerolaattojen avaamisesta seuraa pelin voittaminen (tehty)
* vasemmassa yläkulmassa näkyy montako miinaa on merkkaamatta (tehty)
* keskellä ylhäällä on restart nappi, josta voi aloittaa uuden pelin samalla ruudukolla ja sen vieressä new game nappi, josta voi valita uuden ruudukon
* oikeassa ylänurkassa on suoritukseen kulunut aika sekunteina (tehty)
### Pelin loppumisen jälkeen
* Kun peli loppuu eli käyttäjä joko valitsee miinan tai saa ratkaistua ruudukon eli löytää kaikki oikeassa kohdissa olevat miinat, näytetään highscore lista, ja käyttäjän sijoittuminen sille
* Pelin yläreunassa olevat new game ja restart napit toimivat edelleen
## Jatkokehitysideoita
* Pelin voi viedä verkkoon jolloin sen olisi paremmin saavutettavissa
* Peliin voisi lisätä alkuvalikon ja lisää muita pelejä eli tehdä jonkin laisen pelikonesovelluksen
* miinaharavarn voisi myös toteuttaa esimerkiksi kolmioilla tai viisikulmioilla neliöiden sijasta
* Sovellukseen voisi myös lisätä kaverilistan, jolloin voisi pelata ystäviä vastaan 1v1
