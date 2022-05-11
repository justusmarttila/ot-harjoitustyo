# Miinaharava

## Käyttöohje

Aluksi on login näkymä, josta pääsee kirjautumaan jos on jo käyttäjä, muuten valitse register, jolloin pääsee rekisteröimään uuden käyttäjän.
Tämän jälkeen valitse vaikeustaso ja pääset pelaamaan.
Paina hiiren 1-painiketta (mouse 1) avataksesi laatan tai paina hiiren 2-painiketta merkataksesti miina. Avatun laatan numero kertoo montako miinaa sen ympärillä on.
Vasemmassa ylänurkassa lukee montako miinaa on vielä merkkaamatta eli löytämättä.
Oikeassa ylänurkassa lukee peliisi kulunut aika sekunteina.
Voitat pelin avaamalla kaikki ei-miinat. (Ei ole pakko merkata kaikkia miinoja.

## Dokumentaatio

- [vaatimusmaarittely](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/tyoaikakirjanpito.md)

- [changelog](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/changelog.md)

- [arkkitehtuuri](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/arkkitehtuuri.md)

- [testaus](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/testaus.md)

- [release](https://github.com/justusmarttila/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Asenna riippuvuudet komennolla 
```bash
poetry install
```
2. Alusta tietokanta komennolla
```bash
poetry run invoke build
```
3 Käynnistä sovellus komennolla
```bash
poetry run invoke start
```
## Komentorivitoiminnot
1 Testit suoritetaan komennolla:
```bash
poetry run invoke test
```
2 Testikattavuusraportti generoidaan komennolla
```bash
poetry run invoke coverage-report
```
3 Koodin laadun tarkistaminen
```bash
poetry run invoke lint
```
