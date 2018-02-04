from player import Player
class Location:

    def __init__(self, index, name, points, commands, bdesc, fdesc):
        '''
        Creates a new location object.
        Each object has it's integer "index" which the game refers to usually,
        the string "name" of the location, the integer "points" which may
        potentially be gained when this location is accessed, the list of
        "commands" in this location, its "bdesc" and "fdesc"; brief and long
        description respectively.

        '''
        self.name = name
        self.index = index
        self.points = points
        self.commands = commands
        self.bdesc = bdesc
        self.fdesc = fdesc
        self.visited = False

    def get_name (self):
        '''Returns str brief description of location.'''
        return self.name

    def get_brief_description (self):
        '''Returns str brief description of location.'''
        return self.bdesc

    def get_full_description (self):
        '''Returns str long description of location.'''
        return self.fdesc

    def available_actions(self):
        '''
        Returns the list of the available actions in this location.
        '''
        return self.commands

class Item:

    def __init__ (self, name, start, target, target_points, weight, usable, desc):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, the
        integer target_points being the number of points player gets
        if item is deposited in target location, the integer weight
        of the item, the boolean "usable" if an item can be consumed
        or not and the string "desc", the description of the item.

        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points
        self.weight = int(weight)
        self.useable = usable
        self.desc = desc
        self.drop_loc = -1

    def get_starting_location (self):
        '''
        Returns integer location where item is first found.
        '''
        return self.start


    def get_name(self):
        '''
        Returns the string name of the item.

        Example:
        World.items["calculus textbook"].get_name() = "calculus textbook"

        :return string name of the item
        '''
        return self.name

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''
        return self.target

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''
        return self.target_points

class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...

    def load_map(self, filename):
        '''
        Loads an external file where potential map data is located. It then returns a nested list of integers
        representing locations and the overall map of the game world. The doctest below demonstrates this.

        Example:
        Suppose map.txt is supplied as:
        3 -1 5
        1 4 -1
        2 -1 -1

        Then World.load_map(World, "map.txt") == [[3, -1, 5], [1, 4, -1], [2, -1, -1]]

        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of integers representing map of game world as specified above
        '''
        file = open(filename, 'r')
        self.map = []
        for line in file:
            row = line.split()
            s = 0
            while s < len(row):
                row[s] = int(row[s])
                s += 1
            self.map.append(row)
        file.close()
        return self.map

    def load_locations(self, filename):
        '''
        Stores all locations from filename (locations.txt) into the dictionary "self.locations".
        Each location is created as an object of the Location Class. Each key is based on the location's index.

        Suppose the location file supplied is:
        LOCATION 3
        Path to Campus
        0
        ACTIONS: Follow Glow
        You are currently on the path to campus. Residence is West. The Bus Stop is East.
        As winter settles in, it is dark outside and extremely cold as you are outside. When you glance to the forest, you
        notice a faint, pulsating glow deep within. What on Earth can it be? Curiosity starts to settle in. Anyway, your residence
        is back west, and the bus stop is east.
        END

        Then self.locations == { 3: (location index 3 object here)}

        :param filename: the file from which locations are extracted
        :return: None
        '''
        file = open(filename, 'r')
        self.locations = {}
        for line in file:
            s = ''
            if "LOCATION" in line:
                index = int(line[9:])
                name = file.readline()
                points = int(file.readline())
                r = file.readline()
                if len(r) > 9:
                    r = r.lower()
                    r = r.replace("\n", "")
                    l = r[9:].split(", ")
                    actions = l
                    short = file.readline()
                else:
                    actions = []
                    short = r
                full = file.readline()
                while "END" not in s:
                    full += s
                    s = file.readline()
                location = Location(index, name, points, actions, short, full)
                self.locations[index] = location
        file.close()

    def load_items(self, filename):
        '''
        Stores all items from filename (items.txt) into a dictionary called self.items
        Each item is created as an object of the Item Class. Each key is based on the item's name in lowercase.

        Suppose the text file supplied is:
        NAME: Your Cellphone
        1 39 750 0 Y
        One of your most prized possessions, it has finally done charging. Did you check your missed texts?
        END

        NAME: Ned's Gadget
        3 14 500 0 N
        You have absolutely no idea how to operate this thing. Better return it to Ned ASAP! He knows what he's doing.
        END

        Then self.items == { your cellphone: (cellphone item object here), ned's gadget: (ned's gadget object here)}

        :param filename: the file from which item data is extracted
        :return: None
        '''
        file = open(filename, 'r')
        self.items = {}
        for line in file:
            s = ''
            if "NAME:" in line:
                name = line[6:-1]
                name = name.lower()
                r = file.readline()
                r = r.split()
                start = int(r[0])
                target = r[1]
                tar_loc = r[2]
                weight = r[3]
                if r[4] == "Y":
                    useable = True
                else:
                    useable = False
                desc = file.readline()
                while "END" not in s:
                    desc += s
                    s = file.readline()
                item = Item(name, start, target, tar_loc, weight, useable, desc)
                self.items[name] = item
        file.close()

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Returns a Location object associated with this location if it does. Else, returns None, including -1.
        Suppose were using the same data of load_map and load_location:

        World.get_location(World, 0, 0) == World.locations(self)[3]

        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

        r = self.map[y][x]
        if r == -1:
            return None
        elif r not in self.locations:
            return None
        else:
            return self.locations[r]