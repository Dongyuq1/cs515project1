# Text Adventure Game

This is a simple text adventure game, where the player navigates a series of rooms and interacts with objects in the game world.

## Author

- Name: Yuqi Dong
- Stevens login: ydong28
- Github URL: 
- Estimated project hours: 6h

## How to Play

1. Make sure you have Python installed.
2. Download the game files.
3. Open a command prompt or terminal window in the game directory.
4. Run the game with the command `python game.py <filename>`, where `<filename>` is the name of the JSON file containing the game data.
5. Follow the on-screen prompts to play the game. The commands are not case-sensitive.

## Commands

- `look`: displays the name and description of the current room, as well as any items and exits.
- `go <direction>`: moves the player in the specified direction, if there is an exit in that direction.
- `get <item>`: adds the specified item to the player's inventory, if it is present in the current room.
- `drop <item>`: removes the specified item from the player's inventory and places it in the current room.
- `inventory`: displays the contents of the player's inventory.
- `quit`: exits the game.
- `help`: displays a list of available commands.

## Game Map Data Format

The game data is stored in a JSON file, and consists of an array of rooms, room numbers start at 0. Each room has the following properties:

- `name`: a string containing the name of the room.
- `desc`: a string containing the description of the room.
- `exits`: an object containing key-value pairs that map directions to room indices.
- `items` (optional): an array of strings containing the names of items in the room.
- `locked` (optional): a boolean flag indicating whether the room is locked.

## Example Game Map - map.json

The map has 9 rooms and numbered from 0 to 8. 

Room 2 "The Crypt" contains "master-key". 

Room 7 "The Laboratory" and room 4 "The Tower" are locked.

## Game Extensions

This project has three extensions:

1. `help`: This extension allows the user get a list of available commands.
2. `drop`: This extension allows the user drop an item in their inventory, the name of which can be specified by the user, but it has to be the name of the item in the room. Dropped item will disappear from the inventory of user and rejoin the items of the room.
3. `locked`: This extension locks the room that have "locked" and "up" key-value pair. If the user has not got a "master key" in his or her inventory, he or she cannot enter the locked room.

## Code Test

Test manually using the command line.
Test whole process and look, go, get, drop, inventory, help, drop, locked, quit
1. Start in "The Entrance Hall" -> display the name and description of the current room, as well as any items and exits.
2. `look` -> display same description again.
3. `help` -> display a list of available commands.
4. `inventory` -> Print "You're not carrying anything."
5. `get health-potion` -> Print "You pick up the health-potion."
6. `get dagger` -> Print "You pick up the dagger."
7. `inventory` -> Print "Inventory: health-potion dagger"
8. `look` -> display same description but without "dagger" and "health-potion" in items of the room.
9. `drop health-potion` -> Print "You drop the health-potion."
10. `drop dagger` -> Print "You drop the dagger."
11. `inventory` -> Print "You're not carrying anything."
12. `look` -> display same description and with "dagger" and "health-potion" in items of the room again.
13. `go east` -> Print "You can't go that way."
14. `go south` -> go to room 2 "The Crypt", and display the details of this room
15. `go north` -> Print "The room is locked. You need the master key to enter."
16. `get master-key` -> Print "You pick up the master-key."
17. `go north` -> go to locked room 7 "The Laboratory", and display the details of this room
18. `go` -> Print "Invalid command. Use 'go direction'."
19. `go home` -> Print "You can't go that way."
20. `get` -> Print "Invalid command. Use 'get item'."
21. `get Money` Print "There's no money anywhere."
22. `drop` -> Print "Invalid command. Use 'drop item'."
23. `drop Money` -> Print "You don't have money."
24. `look home` -> Print "Invalid command."
25. `help home` -> Print "Invalid command."
26. `inventory full` -> Print "Invalid command."
27. `^D` -> Print "Use 'quit' to exit."
28. `quit` -> Print "Goodbye!" and end the game.

## Bugs or Issues

No

## Difficult Issues or Bugs and How Resolved

It should be `help` part, `help` verb must not simply be static text, but should be generated from the verbs that have defined. After many attempts, I finally select `inspect` module. In case I don't want to change the function name, I print the function comment to satisfy the help requirement.
