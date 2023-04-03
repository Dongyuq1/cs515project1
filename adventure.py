import inspect
import json
import sys

if len(sys.argv) < 2:
    print('Usage: python program.py <filename>')
    print()
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'r') as f:
    data = json.load(f)


def display_room(room):
    """
    look
    """
    print("> " + room['name'])
    print()
    print(room['desc'])
    print()
    if 'items' in room and room['items']:
        print('Items:', ' '.join(room['items']))
        print()
    print('Exits:', ' '.join(room['exits']))
    print()


def go_direction(command, current_room, inventory):
    """
    go ...
    """
    # Parse the command string to extract the direction
    parts = command.split()
    if len(parts) != 2 or parts[0] != 'go':
        print("Sorry, you need to 'go' somewhere.")
        return current_room

    direction = parts[1]
    # Check if the current room has an exit in the specified direction
    if direction in current_room['exits']:
        next_room_index = current_room['exits'][direction]
        next_room = data[next_room_index]

        # Check if the next room is locked
        if 'locked' in next_room:
            # Check if the player has the master-key
            if 'master-key' in inventory:
                # Move to the next room
                print('You go', direction + '.')
                print()
                display_room(next_room)
                return next_room
            else:
                print("The room is locked. You need the master key to enter.")
                return current_room
        else:
            # Move to the next room
            print('You go', direction + '.')
            print()
            display_room(next_room)
            return next_room
    else:
        print("There's no way to go", direction + '.')
        return current_room


def get_item(command, current_room, inventory):
    """
    get ...
    """
    parts = command.split()
    if len(parts) != 2 or parts[0] != 'get':
        print("Sorry, you need to 'get' something.")
        return current_room, inventory
    item_name = parts[1]

    # Check if the item is in the current room
    if 'items' in current_room and item_name in current_room['items']:
        # Remove the item from the room and add it to the player's inventory
        current_room['items'].remove(item_name)
        inventory.append(item_name)
        print('You pick up the', item_name + '.')
        return current_room, inventory
    else:
        print("There's no", item_name, "anywhere.")
        return current_room, inventory


def drop_item(command, current_room, inventory):
    """
    drop ...
    """
    parts = command.split()
    if len(parts) != 2 or parts[0] != 'drop':
        print("Sorry, you need to 'drop' something.")
        return current_room, inventory
    item_name = parts[1]

    # Check if the item is in the player's inventory
    if item_name in inventory:
        # Remove the item from the inventory and add it to the current room
        inventory.remove(item_name)
        if 'items' in current_room:
            current_room['items'].append(item_name)
        else:
            current_room['items'] = [item_name]
        print('You drop the', item_name + '.')
        return current_room, inventory
    else:
        print("You don't have", item_name + '.')
        return current_room, inventory


def inventory_items(current_room, inventory):
    """
    inventory
    """
    if not inventory:
        print("You're not carrying anything.")
    else:
        print("Inventory:")
        for item in inventory:
            print("  " + item)
    return current_room, inventory


def quit_game():
    """
    quit
    """
    print("Goodbye!")
    sys.exit(0)


def help_command():
    """
    help
    """
    current_module = sys.modules[__name__]
    function_list = [o for o in inspect.getmembers(current_module) if inspect.isfunction(o[1])]

    for function in function_list:
        print(inspect.getdoc(function[1]))


# Start in the first room
current_room = data[0]
inventory = []
display_room(current_room)

while True:
    try:
        command = input('What would you like to do? ').lower()
    except EOFError:
        print()
        print("Use 'quit' to exit.")
        continue
    if command == 'look':
        display_room(current_room)
    elif command.startswith('go'):
        current_room = go_direction(command, current_room, inventory)
    elif command.startswith('get'):
        current_room, inventory = get_item(command, current_room, inventory)
    elif command.startswith('drop'):
        current_room, inventory = drop_item(command, current_room, inventory)
    elif command == 'inventory':
        inventory_items(current_room, inventory)
    elif command == 'quit':
        quit_game()
    elif command == 'help':
        help_command()
    else:
        print("Invalid command.")
