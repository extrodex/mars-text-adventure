import variables
import os
import time
from colorama import Fore
def room1():
  os.system('clear')
  print('''
   ___ ___   ____  ____    _____
  |   |   | /    ||    \  / ___/
  | _   _ ||  o  ||  D  )(   \_ 
  |  \_/  ||     ||    /  \__  |
  |   |   ||  _  ||    \  /  \ |
  |   |   ||  |  ||  .  \ \    |
  |___|___||__|__||__|\_|  \___|

  ''')
  a = input(
      f"{Fore.WHITE}You are in a bright room and you can't see much. The ground is orangish red. You have a vauge memory of Elon Musk sending you on a mission to Mars. You can make out 2 doors with signs in strange charachters you have never seen before. You can either go to the door to the north or the door to the south.\n"
  )
  if "north" in a.lower():
    room2()
  elif "south" in a.lower():
    room3()
  elif "habajab" == a.lower() or "lemmy" == a.lower():
    print("You have found the secret ending!")
    time.sleep(2)
    secret()
  else:
    print("Sorry, I don't understand. Please enter something else")
    room1()


def room2():
  os.system('clear')
  a = input(
      "You open the door and see an expance of redish orangeish ground. You see some massive cyberpunk-looking buildings. There are three buildings you can go into besides the one you just left (building 1 is the one you started in), and there is one giant glass dome. Where do you want to go? Ex:Building 1, Building 2 etc.\n"
  )

  if "building 1" in a.lower():
    room1()
  elif "building 2" in a.lower():
    building2()
  elif "building 3" in a.lower():
    building3()
  elif "building 4" in a.lower():
    building4()
  elif "dome" in a.lower():
    research()
  else:
    print("I don't understand. Please enter something else")
    room2()


def room3():
  os.system('clear')
  a = input(
      "You open the door and it reveals a closet with many things. You can either leave the room or search the closet.\n"
  )
  if "leave" in a.lower():
    room1()
  elif "search" in a.lower():
    a = input(
        "You look around the closet and sift through the many things inside of it. You find a sticky note in the back with the numbers \'1479\'\nenter in \'back\' to go back into the first room\n"
    )
    if "back" in a.lower():
      room1()
    else:
      print("Sorry, I don't understand. Please enter something else")
      room3()
  else:
    print("Sorry, I don't understand. Please enter something else")
    room3()


def building2():
  os.system('clear')
  a = input(
      "You open the door and are met with a darkness. There doesn't seem to be anything of interest. You can inspect the room, or leave.\n"
  )
  if "inspect" in a.lower():
    a = input(
        "You feel around the room and stumble upon a light switch. You flip it on. You see rusted tin walls and a table sitting in the corner. There is something on the table. You pick it up. It looks like some sort of card for something You put it in your pocket. Type \'leave\' to leave the room.\n"
    )
    variables.keycard = True
    if "leave" in a.lower():
      room2()
    else:
      print("Sorry, I don't understand. Please enter something else")
      building2()

  elif "leave" in a.lower():
    room2()
  else:
    print("Sorry, I don't understand. Please enter something else")
    building2()


def building3():
  os.system('clear')
  a = input(
      "You open up the door and you see a bunch of pipe lines. There is a strange substance splattered on the floor. You here a hissing sound from the pipes. It might be dangerous. You can either inspect the room further, or leave\n"
  )
  if "inspect" in a.lower():
    a = input(
        "You look around the room and you see a mysterious red container sitting on the floor. You pick it up. There is a door in the back. You can either leave or inspect the door.\n"
    )
    variables.gascan = True
    if "leave" in a.lower():
      room2()
    elif "inspect" in a.lower() or "door" in a.lower():
      if variables.keycardScaned == True:
        wing()
      else:
        os.system('clear')
        print("This door is locked")
        time.sleep(1)
        building3()
    else:
      print("Sorry, I don't understand. Please enter something else")
      building3()
  elif "leave" in a.lower():
    room2()
  else:
    print("Sorry, I don't understand. Please enter something else")
    building3()


def building4():
  os.system('clear')
  a = input(
      "You open the door and see a bunch of racks. You see some boxes. You can either inspect the boxes or leave\n"
  )
  if "inspect" in a.lower():
    a = input(
        "You look around the boxes and you see a strange tool. You pick it up. It is heavy. Type \'leave\' to leave the room\n"
    )

    variables.gun = True
    if "leave" in a.lower():
      room2()
    else:
      print("Sorry, I don't understand. Please enter something else")
      building4()
  elif "leave" in a.lower():
    room2()
  else:
    print("Sorry, I don't understand. Please enter something else")
    building4()


def research():
  os.system('clear')
  a = input(
      "You walk up to the glass dome. You try to open up the door but it is locked. There is a keypad next to the door. You can either enter in the code or leave. What do you want to do?\n"
  )
  if "code" in a.lower():
    a = input(
        "You turn the keypad on. A dim display appears. It says \'Please enter code\'\n"
    )
    if a == "1479":
      print(
          "The screen flashed green. The door swings open. In the middle there is a thing that looks like a scanner next to a computer. You turn the scanner on.\n"
      )
      scan()
    else:
      print(
          "The screen flashed red. Then some strange force knocks you away from the dome.\n"
      )
      room2()
  elif "leave" in a.lower():
    room2()
  else:
    print("Sorry, I don't understand. Please enter something else")
    research()


def scan():
  a = input(
      "What would you like to scan? Enter in \'inv\' for your items. Enter in \'leave\' to leave\n"
  )
  if "card" in a.lower() and variables.keycard == True:
    a = input(
        f"{Fore.BLUE}You put the card on the scanner. After waiting for a few seconds the computer lights up. It says \'This is a wing keycard. It may be used to access the wing room with the spaceships\' Would you like to scan another item? Yes or leave\n"
    )
    variables.keycardScaned = True
    if "yes" in a.lower():
      scan()
    elif "leave" in a.lower():
      room2()
    else:
      print("Sorry, I don't understand. Please enter something else")
      scan()
  elif "container" in a.lower() and variables.gascan == True:
    a = input(
        f"{Fore.BLUE}You put the container on the scanner. After waiting for a few seconds the computer lights up. It says \' This container has gas inside. It is used to fuel spaceships\' Would you like to scan another item? Yes or leave. Enter in \'leave'\ to leave\n"
    )
    variables.gascanScaned = True
    if "yes" in a.lower():
      scan()
    elif "leave" in a.lower():
      room2()
    else:
      scan()
  elif "leave" in a.lower():
    room2()
  elif "tool" in a.lower() and variables.gun == True:
    a = input(
        f"{Fore.BLUE}You put the tool on the scanner. After waiting for a few seconds the computer lights up. It says \'This tool is a evaporation gun. Whoever it us used on evaporites into thin air.\' Would you like to scan another item? Yes or leave. Enter in \'leave'\ to leave\n"
    )
    variables.gunScaned = True
    if "yes" in a.lower():
      scan()
    elif "leave" in a.lower():
      room2()
    else:
      print("Sorry, I don't understand. Please enter something else")
      scan()
  elif "inv" in a.lower():
    inventory()
    scan()
  else:
    print("Sorry, I don't understand. Please enter something else")
    scan()


def inventory():
  print("You have:")
  if variables.keycard == True:
    print("A card")
  if variables.gascan == True:
    print("A container")
  if variables.gun == True:
    print("A tool")
  return


def wing():
  a = input(
      "You scan the keycard and the door opens. You walk into the wing. There is a giant spaceship in the middle of the room. Would you like to leave or inspect the spaceship?\n"
  )
  if "inspect" in a.lower():
    a = input(
        "You walk up to the spaceship. There is a large red button on the side. Would you like to press the button or leave?\n"
    )
    if "press" in a.lower():
      a=input(
          "You press the button. A large door opens up, creating a ramp to get on the spaceship. You walk up the ramp into the spaceship. You walk around the spaceship until you see a room that says \'navigaion\' Would you like to open the door slowly or fast?\n"
      )
      if "slow" in a.lower():
        print("You open the door slowly. There is an alien looking at a control panel.")

        if variables.gunScaned == True and variables.gascanScaned == True:
            print(f"{Fore.GREEN}You shoot the alien. It falls to the floor. You walk up to the control panel fill the fuel tank with fuel. You fly though outer space and land eveuntually on earth. You find Elon Musk and give him a good slap. You win!")
        elif variables.gunScaned == True:
         print(f"{Fore.RED}You shoot the alien. It falls to the floor. You walk up to the control panel and press the button. Nothing happens. It says fuel low. In anger, you press all the buttons on the control panel. The spaceship explodes. You die.")
        else:
           print(f"{Fore.RED}You run up to the alien and tackle him. You wrestle him for a little bit before he throws you off him. He then takes out his gun and shoots you. You die.")
      if "fast" in a.lower():
        a = input(f"{Fore.RED}You open the door fast. It creaks really loudly. An alien looks turns around and shoots you before you have time to react to anything. You die.")
    elif "leave" in a.lower():
      building3()
    else:
      print("Sorry, I don't understand. Please enter something else")
      wing()
  elif "leave" in a.lower():
    building3()
  else:
    print("Sorry, I don't understand. Please enter something else")
    wing()

def secret():
  a=input("Enter in developer command:")
  if "find gun" in a.lower():
    variables.gun=True
    secret()
  elif "scan gun" in a.lower():
    variables.gunScaned=True
    secret()
  elif "find gascan" in a.lower():
    variables.gascan=True
    secret()
  elif "scan gascan" in a.lower():
    variables.gascanScaned=True
    secret()
  elif "find keycard" in a.lower():
    variables.keycard=True
    secret()
  elif "scan keycard" in a.lower():
    variables.keycardScaned=True
    secret()
  elif "exit" in a.lower():
    room1()
  else:
    print("invalid command")
    secret()
room1()
