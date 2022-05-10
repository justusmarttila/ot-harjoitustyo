# Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen tarkoitus on kehittää käyttäjän matemaattista hahmotuskykyä ja tuottaa mielihyvää pelaamalla Miinaharavaa.
Monet ovat kertoneet, että pelit ovat auttaneet rentoutumaan ja ottamaan ajatukset irti stressaavasta arjesta.
## Käyttäjät
Käyttäjä voi kirjautua eri käyttäjille ja pelata peliä.
## Toiminnallisuudet
### Ennen kirjautumista
* Käyttäjät voi luoda tunnuksen (tehty)
    * Käyttäjätunnuksen tulee olla uniikki (tehty)
* Tunnuksien avulla voidaan kirjuatua (tehty)
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
* Kun peli loppuu eli käyttäjä joko valitsee miinan tai saa ratkaistua ruudukon eli löytää kaikki oikeassa kohdissa olevat miinat, kerrotaan pelaajalle voittiko hän vai hävisikö ja kuinka kauan peli kesti
* Pelin yläreunassa olevat new game ja restart napit toimivat edelleen
## Jatkokehitysideoita
* Suoritusaikoja voidaan kartoittaa ja liittää käyttäjätunnuksiin
* Pelin voi viedä verkkoon jolloin sen olisi paremmin saavutettavissa
* Peliin voisi lisätä alkuvalikon ja lisää muita pelejä eli tehdä jonkin laisen pelikonesovelluksen
* miinaharavarn voisi myös toteuttaa esimerkiksi kolmioilla tai viisikulmioilla neliöiden sijasta
* Sovellukseen voisi myös lisätä kaverilistan, jolloin voisi pelata ystäviä vastaan 1v1
