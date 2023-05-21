# README

## Video Presentation of Terminal Application

[Video Presentation link](https://youtu.be/0Op9-XwxEKg)

## (R3) Attributions

### ASCII art:

All ASCII art was sourced from the [ASCII Art Archive](https://www.asciiart.eu/) and the [ASCII.co.uk](https://ascii.co.uk/). Artist signatures were retained on the artwork as per the websites' respecitive use policies.

## (R4) Source Control Repository

[GitHub Repository link](https://github.com/kalfung/KaloonFung_T1A3)

## (R5) Code styling

Throughout this application, I have adhered to the guidelines outlined by van Rossum et al in [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/).

- Lines of code do not exceed 79 characters in length
- Functions and variable names do not contain any unncessary capitals, and;
- Empty lines have been utilised where necessary.

## (R6) Features 

### Neverending dungeon adventure game

The game uses classes, loops and conditional control structures to create generate endless encounters with monsters, treasure coffers and traps.

### Battle mechanics

I've created methods for various classes to allow you to battle monsters as you encounter them, and cast spells to restore your health and ensure your survival!

### Loot mechanics

You may encounter treasure coffers that can will reward players handsomely when looted. But some of these may hide deadly traps. Various methods have been implemented to enable players to loot these coffers.

### ASCII artwork and colour

The game uses ASCII art and coloured text to add to the atmosphere of the player's experience. The application handles multiple text files to present the ASCII artwork to players at certain points in the game.

## (R7) Implementation Plan

A link to my [Implementatiopn Plan on Trello](https://trello.com/b/38r4jreP/t1a3-terminal-application)

Throughout the development of the game, I made use of Trello to track and prioritise features and components of the application, especially those with dependencies. 



## (R8) Help Documentation

### Dependencies
The game makes use of just two Python packages in order to operate properly. A list of these dependencies can be found in the requirements.txt file included, but they're listed here for convenience:

- art==5.9
- colorama==0.4.6

These should be automatically installed when running of the provided bash script mentioned above. However, if you'd like to install them manually via your terminal, you may do so by navigating to the game's 'src' directory, create and activate a virtual environment, and enter the following to install the required packages:

```pip3 install -r requirements.txt```

### System Requirements

Because there are no images or sound produced when running the game, any modern PC from the past 10 years should suffice. The application does not have any high CPU, GPU or memory requirements.

To run the game, users will simply need an operating system that supports the use of a Terminal or Command Line Interface, such as Linux. If you are using a Windows computer, it is recommened that you use the Ubuntu terminal environment by installing the Windows Subsystem for Linux (WSL).

### How to play the game

Once you have run one of the provided bash scripts and the required packages have been installed, the game will run. The text will provide you with instructions with options highlighted in colour to guide you on how to proceed through the dungeon. The game takes simple text input from the player and randomises their encounters.

The game will end when the player is defeated in battle against a monster, or if they choose to stop before the next encounter. Try your best to develop a strategy during the monster battles (there's no running from the fights!), collect as much treasure as possible, and spot the traps!

