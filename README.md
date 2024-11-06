# Pac-Man Hra v Pythonu (Pygame)

Tento projekt je jednoduchá hra Pac-Man vytvořená pomocí Pythonu a knihovny Pygame. Ve hře ovládáte Pac-Mana, pohybujete se po mapě, sbíráte všechny tečky a vyhýbáte se překážkám (zdím). Hra zobrazuje skóre a umožňuje restart po vítězství.

## Vlastnosti

- Pohyb Pac-Mana pomocí šipek
- Herní mapa s překážkami a tečkami
- Systém skóre a vítězná zpráva při dosažení cíle
- Možnost restartu hry po vítězství stiskem klávesy `R`

## Jak spustit hru

1. Ujistěte se, že máte nainstalovanou knihovnu **Pygame**:
   ```bash
   pip install pygame
    ```

2. Spusťte skript:
   ```bash
   python pacman.py
   ```

## Ovládání
- **Šipky**: Pohyb Pac-Mana
- **R**: Restart hry po výhře

## Popis kódu
- **Konstanty a barvy**: Jsou definovány základní herní parametry, jako je velikost dlaždic (`TILE_SIZE`) a barvy jednotlivých prvků.
- **Mapová struktura (`MAP_LAYOUT`)**: Dlaždice na mapě jsou definovány jako pole s hodnotami, kde `1` označuje zeď a `2` tečku.
- **Třída `PacMan`**: Obsahuje funkce pro pohyb Pac-Mana a vykreslení jeho pozice.
- **Funkce `draw_map()`**: Vykreslí herní mapu s překážkami a tečkami.
- **Funkce `check_dot_collision()`**: Kontroluje, zda Pac-Man narazil na tečku, a aktualizuje skóre a počet zbývajících teček.
- **Hlavní smyčka (`game_loop`)**: Zajišťuje vykreslování, ovládání, pohyb Pac-Mana a kontrolu vítězství.

## Herní logika
1. Hra načte mapu a vykreslí ji.
2. Pac-Man se pohybuje po mapě dle stisknutých kláves, přičemž nesmí projít zdí.
3. Při střetu s tečkou se bod přičítá ke skóre a tečka mizí z mapy.
4. Hráč vyhrává, pokud seberete všechny tečky, po čemž se zobrazí výherní zpráva a možnost restartu hry.

## Požadavky
- Python 3.x
- Knihovna Pygame

## Licence
Tento projekt je k dispozici pod licencí MIT.
