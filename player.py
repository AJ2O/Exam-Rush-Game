class Player:

    def __init__(self, x, y):
        '''
        Creates a new Player with initial x and y coordinates,
        a score, hypothermia levels, a timer, a weight due to
        items, a timer for boosting items, an inventory of items,
        notes they have taken, past choices made and their victory state.
        :param x: starting x-coordinate of position on map
        :param y: starting y-coordinate of position on map
        :return:
        '''
        self.x = x
        self.y = y
        self.score = 0
        self.hypothermia = 0
        self.timer = "5:00"
        self.weight = 0
        self.choc_timer = 0
        self.inventory = {}
        self.notes = []
        self.past_choices = []
        self.past_places = ["Wall"]
        self.victory = False

    def set_pos(self, dx, dy):
        '''
        Given integers dx and dy, this function transports player to a new location.

        Example:
        Player.x = 0
        Player.y = 0

        Player.set_pos(1, 3)
        Player.x == 1
        Player.y == 3

        :param dx: the x-coordinate of the desired location
        :param dy: the y-coordinate of the desired location
        :return:

        '''
        self.x = dx
        self.y = dy

    def move(self, dx, dy):
        '''
        Given integers dx and dy, they add to the player's current x and y positions to move the player
        to a new location.

        The doc test below demonstrates how the player's coordinates shift.

        :param dx:
        :param dy:
        :return:

        >>> p = Player(0,0)

        >>> p.move_north()

        >>> p.move_north()

        >>> p.move_east()

        >>> p.x == 1
        True

        >>> p.y == -2
        True

        '''
        self.x += dx
        self.y += dy

    def move_north(self):
        '''
        These integer directions are based on how the map must be stored
        in our nested list World.map

        The demonstration of these functions can be seen in the doc test in the "move" function.
        '''
        self.move(0,-1)

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(1,0)

    def move_west(self):
        self.move(-1,0)

    def add_item(self, item):
        '''
        Adds item to player's inventory.
        :param item: the item to be added in the form of a string
        :return:
        '''
        self.inventory[item.name] = item

    def remove_item(self, item):
        '''
        Removes requested item from the player's inventory.
        :param item: the item to be removed
        :return:
        '''
        del(self.inventory[item.name])

    def get_inventory(self):
        '''
        Returns the inventory of the player.
        :return: the formatted inventory of the player
        '''
        print("Inventory")
        s = ""
        for x in self.inventory:
            s = s + " | " + x
        return s
