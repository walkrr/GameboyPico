# RPi Pico Game Boy ROM Loader

This project allows you to use a Raspberry Pi Pico as a ROM chip for running Game Boy games on a console. It utilizes a [Game Boy breakout board](https://github.com/Gekkio/gb-hardware/tree/master/GB-BRK-CART) and is based on [PicoROM](https://github.com/nickbild/picoROM). The repo contains scripts that convert a `.gb` ROM file into a C file, which is then included when building PicoROM. The resulting `u2f` file loads the ROM when the Pico is connected to a Game Boy using the breakout cart.

## Prerequisites

- Raspberry Pi Pico
- [Game Boy breakout board](https://github.com/Gekkio/gb-hardware/tree/master/GB-BRK-CART)

## Wiring

Connect the Pico to the Game Boy breakout board as follows:

| Pico GPIO Pin | GB Breakout Cart Pin |
|---------------|----------------------|
| 0             | Address0             |
| 1             | Address1             |
| 2             | Address2             |
| 3             | Address3             |
| 4             | Address4             |
| 5             | Address5             |
| 6             | Address6             |
| 7             | Address7             |
| 8             | Address8             |
| 9             | Address9             |
| 10            | Address10            |
| 11            | Address11            |
| 12            | Address12            |
| 13            | Address13            |
| 14            | Address14            |
| 15            | Data0                |
| 16            | Data1                |
| 17            | Data2                |
| 18            | Data3                |
| 19            | Data4                |
| 20            | Data5                |
| 21            | Data6                |
| 22            | Data7                |

## Usage

1. Clone this repository and the PicoRom repository
2. Navigate to the roms directory in this repo
3. Place your .gb rom in this roms directory
4. Run 'python gb2array.py {your rom filename here}  > {rom name}.txt'
5. Copy the contents of the text file to the portion of picoROM rom.c setup_rom_conents function at line 122, after the comment saying "Program, starting at ROM address 0."
3. Build PicoROM
4. Load the resulting `u2f` file onto your Pico
5. Connect the Pico to the Game Boy console using the breakout cart
