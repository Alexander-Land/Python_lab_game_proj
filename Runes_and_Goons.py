import random
import math


# todo 
# combat
# add print statements to spells, weapons, and enemies
# player health
# fix spells in rooms dict
# win loss



#room handling
class map(object):
    """creates a map of the game
    contains every item and enemy in every room. 
    the data will be saved in the self.rooms dictionary"""
    def __init__(self):
        self.rooms = {}

    def loadsavedgame(self):
        pass #open json and fill self.rooms

    def loadnewgame(self):
        self.rooms = {'Starting Room': {'East': 'The Drowned Gate', #Home of the Game
                                        'South': 'The Embered Threshold',
                                        'West': 'Ancient Convergence',
                                        'Item': {'name' : 'Rusty Sword',
                                                'damage': 5,
                                                'speed': 1,
                                                'type':'weapon'},

                                        },
                                        

                    'The Embered Threshold': {'North': 'Starting Room', #Fire Area
                                            'East': 'Smoldering Ascent',
                                            'South': 'Magma Crucible',
                                            'West': 'Stormfire Bastion',
                                            'Item': {'name': 'Fireball',
                                                     'damage': 5,
                                                     'speed': 1,
                                                     'type': 'spell'},
                                            'Enemy': {'name': 'Goblin',
                                                  'health': 10,
                                                    'weakness': 'water',
                                                    'damage': 2,
                                                    'speed': 1,
                                                    'speech': 'Oh, you actually think you stand a chance? Cute. Now, lets see if you can dodge *this!*'}
                                                    },

                    'Stormfire Bastion': {'East': 'The Embered Threshold',
                                        'Item': {'name':'Blazing Maelstrom',
                                                 'damage': 10,
                                                 'speed': 2,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Fire Elemental',
                                                  'health': 100,
                                                  'weakness': 'water',
                                                  'damage': 5,
                                                  'speed': 1,
                                                  'speech': 'You dare to challenge me? You will be reduced to ashes!'}
                                        },

                    'Magma Crucible': {'North': 'The Embered Threshold',
                                        'Item': {'name':'Volcanic Maul',
                                                'damage': 15,
                                                 'speed': 2,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Lava Golem',
                                                  'health': 150,
                                                  'weakness': 'water',
                                                  'damage': 10,
                                                  'speed': 1,
                                                  'speech': 'You are not worthy to face me! Prepare to be melted down!'},
                                        },

                    'Smoldering Ascent': {'West': 'The Embered Threshold',
                                        'Item': {'name':'Inferno Fang',
                                                 'damage': 20,
                                                 'speed': 3,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Fire Dragon',
                                                  'health': 200,
                                                  'weakness': 'water',
                                                  'damage': 20,
                                                  'speed': 1,
                                                  'speech': 'You are brave to face me, but you will be reduced to ashes!'},
                                        },

                    'The Drowned Gate': {'West': 'Starting Room', #Water Area
                                        'South': 'Frozen Depths',
                                        'East': 'Whirlpool Shrine',
                                        'North': 'Abyssal Cavern',
                                        'Item': {'name':'Water Blast',
                                                    'damage': 5,
                                                    'speed': 1,
                                                    'type': 'spell'},
                                        'Enemy': {'name': 'Mermaid',
                                                  'health': 10,
                                                  'weakness': 'fire',
                                                  'damage': 2,
                                                  'speed': 1,
                                                  'speech': 'You dare to challenge me? You will be drowned!'},
                                                                    },
                                                

                    'Abyssal Cavern': {'South': 'The Drowned Gate',
                                    'Item': {'name':'Abyssal Trident',
                                             'damage': 10,
                                             'speed': 1,
                                             'type': 'weapon'},
                                    'Enemy': {'name': 'Siren',
                                              'health': 100,
                                              'weakness': 'fire',
                                              'damage': 5,
                                              'speed': 1,
                                              'speech': 'You are not worthy to face me! Prepare to be drowned!',
                                              },
                                    },

                    'Frozen Depths': {'North': 'The Drowned Gate',
                                    'Item': {'name':'Glacier Fang',
                                             'damage': 15,
                                             'speed': 2,
                                             'type': 'weapon'},
                                    'Enemy': {'name': 'Ice Golem',
                                              'health': 150,
                                              'weakness': 'fire',
                                              'damage': 10,
                                              'speed': 1,
                                              'speech': 'You are brave to face me, but you will be frozen solid!'}
                                    },

                    'Whirlpool Shrine': {'West': 'The Drowned Gate',
                                        'Item': {'name':'Whirlpool Staff',
                                                 'damage': 20,
                                                 'speed': 3,
                                                 'type': 'weapon'},
                                        'Enemy': {'name': 'Water Elemental',
                                                  'health': 200,
                                                  'weakness': 'fire',
                                                  'damage': 20,
                                                  'speed': 1,
                                                  'speech': 'You are brave to face me, but you will be drowned!'}
                                        },

                    'Ancient Convergence': {'East': 'Starting Room',
                                            'Enemy': {'name': 'Ancient Guardian',
                                                      'health': 1000,
                                                      'weakness': 'none',
                                                      'damage': 50,
                                                      'speed': 1,
                                                      'speech': 'You have come far, but you will not pass!'}
                                                      },
                      #end of game area, final boss
        }
        self.current_room = 'Starting Room'
        self.previous_room = 'Starting Room'

def move():
    """when called it'll ask the player which room they want to move to and allow them to move there
    Also doesn't allow illegal movement"""
    directions = ["North", "South", "East", "West"]

    while True:
        print(f"You're in the {mapinstance.current_room}")

        print(f"These are the rooms connected to the room you're in: \n")
        for (nav, room) in mapinstance.rooms[mapinstance.current_room].items():
            if nav in directions:
                print(f"{nav}: {room}")

        desired_direction = str(input("\n type the direction you want to move: ")).title()

        if desired_direction in directions and desired_direction in mapinstance.rooms[mapinstance.current_room]:
            mapinstance.previous_room = mapinstance.current_room
            mapinstance.current_room = mapinstance.rooms[mapinstance.current_room][desired_direction]
            print("-"*50)
            print(f"\n\nYou walk into: {mapinstance.current_room}")

            break
        else:
            print("\nThere is no room in that direction \nPlease type a valid direction")
            print("------------------------------------------------------------------------------------\n")

class player(object):
    """creates player object to store data"""
    def init(self, name, health, damage, max_health):
        self.name = name
        self.health = health
        self.damage = damage
        self.max_health = max_health

class enemy(object):
    """creates enemy and manages damage from enemies"""
    def __init__(self,name,health,weakness,damage,speed,speech=None):
        self.name = name
        self.health = health
        self.weakness = weakness
        self.damage = damage
        self.speed = speed
        self.speech = speech
           
    def attack(self,player):
        """attacks player, speed calculations will be done elsewhere"""
        player.health -= self.damage

    def speak(self):
        """prints the saved line that the creature would say"""
        print("\"", self.speech,"\"")

class weapons(object):
    """creates weapon for warrior"""
    def __init__(self, name, damage, speed):
        self.name = name
        self.damage = damage
        self.speed = speed

    def attack(self, enemy):
        enemy.health -= self.damage
        
        speed_diff = self.speed - enemy.speed
        if speed_diff > 0:
            probability_of_second_hit = 1 / (1 + math.exp((3-speed_diff)))
            if probability_of_second_hit*100 > random.randint(1,100):
                enemy.health -= self.damage
        # if speed difference is great enough the weapon has a chance to hit twice.

class spells(object):
    """Creates spells for wizard
    spells have a damage value and an element"""
    def __init__(self,name,damage,element):
        self.name = name
        self.damage = damage
        self.element = element

    def attack(self, enemy):
        """deals damage to enemy depending on elemental weakness"""
        if self.element == enemy.weakness:
            enemy.health -= self.damage*1.5
        else:
            enemy.health -= self.damage


class equipment_inventory(object):
    """spells and weapons are equipment for attacking
    this class will handle which equipment the player has and using the weapons"""
    def __init__(self):
        self.weapons_and_spells = {}
        self.duplicate_itemduplicate_item = False
        self.healing_potions = 0


    def get_equipment(self, equipment_name, type, attributes = None):
        """adds equiment based on type"""

        self.duplicate_itemduplicate_item = False

        for entry in self.weapons_and_spells:
            if entry['name'] == str(equipment_name):
                print(f'you got a {equipment_name} but you already had one so it was thrown away.')
                self.duplicate_item = True
    
        if not self.duplicate_item:
            self.weapons_and_spells[equipment_name]={'type':type, 'attributes': attributes}
    
    def useHealPotion(self):
        if self.healing_potions > 1:
            self.healing_potions -= 1
            playerinstance.health = playerinstance.max_health
            print(f'You have {self.healing_potions} remaining\n Health restored to {playerinstance.max_health}')

def pickup_items():
    """after ending up in a room run pickup items to allow """
    if 'Item' in mapinstance.rooms[mapinstance.current_room]:
        print(f"\n You found a {mapinstance.rooms[mapinstance.current_room]['Item']['name']}!")
        print("Do you want to pick it up? (y/n)")
        pickup = str(input()).lower()
        if pickup == 'y':
            item_name = mapinstance.rooms[mapinstance.current_room]['Item']['name'] 
            item_type = mapinstance.rooms[mapinstance.current_room]['Item']['type']

            if item_type == 'weapon':
                item_attributes = {'damage':mapinstance.rooms[mapinstance.current_room]['item']['damage'],
                                    'speed':mapinstance.rooms[mapinstance.current_room]['Item']['speed']}
            elif item_type == 'spell':
                item_attributes = {'damage':mapinstance.rooms[mapinstance.current_room]['item']['damage'],
                                     'speed':mapinstance.rooms[mapinstance.current_room]['Item']['element']}
            else:
                pass

            player_inventory.get_equipment(item_name,item_type, item_attributes)

            print(f"You picked up the {item_name}!")
            print("-" * 50)
            del mapinstance.rooms[mapinstance.current_room]['Item']

        else:
            print(f"You left the {mapinstance.rooms[mapinstance.current_room] ['Item']['name']} behind.")
            print("-" * 50)

    if 'healing potion' in mapinstance.rooms[mapinstance.current_room]: 
        player_inventory.healing_potions += mapinstance.rooms[mapinstance.current_room]['healing potion']
        print(f'you found {mapinstance.rooms[mapinstance.current_room]['healing potion']} healing potions!')
        del mapinstance.rooms[mapinstance.current_room]['healing potion']
    
    if not('Item' in mapinstance.rooms[mapinstance.current_room] and 'healing potion' in mapinstance.rooms[mapinstance.current_room]):
            print("There is no item in the room.")
            print("-" * 50)




def combat():
    global gameover

    if "Enemy" in mapinstance.rooms[mapinstance.current_room]:
        current_enemy = enemy(mapinstance.rooms[mapinstance.current_room]["Enemy"]["name"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["health"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["weakness"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["damage"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speed"],
                              mapinstance.rooms[mapinstance.current_room]["Enemy"]["speech"])

        print(f"\nA {current_enemy.name} appeared!!\n")

        print(f"{current_enemy.name}'s stats\n---------------------")
        print(f"health: {current_enemy.health}\ndamage: {current_enemy.damage}\nweakness: {current_enemy.weakness}\nspeed: {current_enemy.speed}\n")

        print(f"You\'re health is currently at: {playerinstance.health} ({100*playerinstance.health/playerinstance.max_health}%)")

        FightorFlee = input("Do you want to fight or run?\nf: fight\nr: run\n")

        if FightorFlee == 'f':
            """fight code"""
            fighting = True
                                # isn't done
                                #select item or heal, attack, take damage, check healths, loop 
            while fighting:
                while True:
                    "selecting item or weapon"
                    AttackorUsePotion = input("Would you like to:\n1: Attack\n2: Use Health Potion")

                    break




                fighting = False


        else:
            """flee code"""
            mapinstance.current_room = mapinstance.previous_room
            print(f'You\'ve fled to the previous room\nCurrent Room: {mapinstance.current_room}')
            return
        
        #win loss handling

    else:
        print(f"There's no enemy in this room")
               








# Start of main code
gameover = False
mapinstance = map()
playerinstance = player(name= ,health= ,damage= , max_health=)    #need to do
player_inventory = equipment_inventory()



