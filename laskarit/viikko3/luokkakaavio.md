```mermaid 
classDiagram
    Pelaaja "*" --> "2-8" Pelilauta
    Noppa "2" --> "2" Pelilauta
    Ruutu "*" --> "40" Pelilauta
    Ruutu "*" --> Pelaaja
    class Pelaaja{
        nimi
        pelinappula
    }
    class Noppa{
        arvo
    }
    class Ruutu{
        nimi
        seuraavaruutu
        pelinappula
    }
    class Pelilauta{
        id
    }
```
