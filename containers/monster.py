import sys
sys.path.append('__HOME__/DEMMO')

from containers.game_object import GameObject

class Monster(GameObject):
    def __init__(self, id, row, col, health, power, is_boss=False, defeated_by=None):
        """
        Initializes a new Monster object
        :param id: (string) id of the monster
        :param row: (int) row of the object
        :param col: (int) col of the object
        :param health: (int) health of the monster, initial health cannot be < 0
        :param power: (int) power of the monster
        :param is_boss: (bool) whether or not the monster is a boss
        :param defeated_by: (set) set of player ids that have defeated it
        """
        # TODO: Complete monster class by adding more fields and adding methods to
        #       interact with a monster
        super().__init__(id, row, col, health, power)
        if not defeated_by:
            defeated_by = set()
        self.is_boss = is_boss
        self.defeated_by = defeated_by

    def get_gold(self):
        base_gold = (self.health + self.power) * 5
        if self.is_boss:
            return 2 * base_gold
        else:
            return base_gold

    def get_is_boss(self):
        return self.is_boss

    def get_defeated_by(self):
        return self.defeated_by

    def get_monster_stats(self):
        """
        :return: this monster's stats in sequence
        """
        return self.get_health(), self.get_power(), self.get_is_boss(), self.get_defeated_by()

    def __str__(self, only_id=False):
        """
        :return: string representation of the game object
        """
        if only_id:
            return self.id

        return "(id: {}, health: {}, power: {}, is boss: {}, defeated by: {})".format(
            self.id, self.health, self.power, self.is_boss, self.defeated_by
        )