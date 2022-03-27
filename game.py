# Class 1: Monsters
# 3 sizes, 3 colors, 3 shapes
# can run away and can attack
# each attack takes away 2 points from hero
# disappear after 1 attack by a hero
class Monster:

  def __init__( self, size, color, shape, points = 2 ):
    self.size = size
    self.color = color
    self.shape = shape
    self.points = points
    self.is_defeated = False
    self.is_disappear = False

  def __repr__(self):
    # printing a robot will print the size, color, and shape)
    return "The hero has met a {size}, {shape}, {color} monster!".format(size = self.size, shape = self.shape, color = self.color)
  
  def defeated(self):
    #attacking a monster will flip its status to True
    self.is_defeated = True
    #a disppeared monster can't have any points
    if self.points != 0:
        self.points = 0
    print("The {size}, {shape}, {color} monster has been defeated!".format(size = self.size, shape = self.shape, color = self.color))

  def disappear(self):
    print("The {size}, {shape}, {color} monster has disappeared!".format(size = self.size, shape = self.shape, color = self.color))

monster_one = Monster("large", "blue", "round")
monster_two = Monster("small", "pink", "square") 
#print(repr(monster_one))
#monster_one.defeated()
#monster_one.disappear()
#print(monster_one.points)
#print(monster_two.is_defeated)

#print(repr(monster_two))
#monster_two.defeated()
#monster_two.disappear()

#print(monster_one.size)
#print(monster_one.points)

# CLass 2: Hero
# 1 size, 1 shape, choice of 3 colors
# can run away and can attack
# start with 20 points 
# earn 2 points for every monster killed
# win when they reach 40 points
#class Hero:
  #def __init__(self, input_size, input_shape, input_color, )
class Hero:
  # name of player
  # number of points
  # number of monsters defeated
  def __init__(self, name, color):
    self.name = name
    self.color = color
    self.num_monsters_defeated = 0
    self.points = 20
    self.is_defeated = False
    self.is_victorious = False

  def __repr__(self):
    return "Welcome hero {name}! Your goal is to defeat monsters and win the game. You have {points}. Each time you defeat a monster, you get 2 points. Each time a monster attacks you, you lose 2 points. You win the game when you reach 40 points! Let the games begin!".format(name = self.name, points = self.points)

  def defeated(self):
    #prints the name of the trainer, number of monsters defeated, and the number of current points. Also prints the number of monsters that need to be defeated to win. 
    return ("The hero {name} has defeated {num_monsters_defeated} monsters and has {points} points.".format(name = self.name, num_monsters_defeated = self.num_monsters_defeated, points = self.points))
    #for needed_points in self.points:
      #return (needed_points == (40 - self.points))
    #return "{needed_points} are needed to win the game!".format(needed_points = needed_points)

  def attack(self):
    return "The hero {name} attacked the {monster}! The hero receives 2 points.".format(name = self.name, monster = monster)


hero_one = Hero("Tina", "teal")
#print(hero_one.name)
#print(hero_one.color)
#print(hero_one.points)
#print(repr(hero_one))
hero_one.defeated()