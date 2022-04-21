# Miinaharava

## Dokumentaatio

- [vaatimusmaarittely](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [changelog](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/changelog.md)

- [arkkitehtuuri](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna riippuvuudet komennolla 

poetry install

## Komentorivitoiminnot

1. Käynnistä sovellus komennolla

poetry run invoke start

2. Testit suoritetaan komennolla:

poetry run invoke test

3. Testikattavuusraportti generoidaan komennolla

poetry run invoke coverage-report

4. Koodin laadun tarkistaminen

poetry run invoke lint
