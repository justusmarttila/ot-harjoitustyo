# Miinaharava

## Käyttöohje

Paina alussa Login nappia ja sitten valitse vaikeustaso

## Dokumentaatio

- [vaatimusmaarittely](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/vaatimusmaarittely.md)

- [tyoaikakirjanpito](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/tyoaikakirjanpito.md)

- [changelog](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/changelog.md)

- [arkkitehtuuri](https://github.com/justusmarttila/ot-harjoitustyo/blob/master/minesweeper-game/dokumentaatio/arkkitehtuuri.md)

- [release](https://github.com/justusmarttila/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Asenna riippuvuudet komennolla 
```bash
poetry install
```
## Komentorivitoiminnot

1. Käynnistä sovellus komennolla
```bash
poetry run invoke start
```
2. Testit suoritetaan komennolla:
```bash
poetry run invoke test
```
3. Testikattavuusraportti generoidaan komennolla
```bash
poetry run invoke coverage-report
```
4. Koodin laadun tarkistaminen
```bash
poetry run invoke lint
```
