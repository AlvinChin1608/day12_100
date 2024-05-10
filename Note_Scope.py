################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # Output 2

increase_enemies()
print(f"enemies outside function: {enemies}") # Output 1

# Local Scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)
# drink_potion() # Output 2
# print(potion_strength) we need to definite this..

# Global Scope
player_health = 10

def game():
  def drink_portion():
    potion_strength = 2
    print(potion_strength)
  drink_portion()
print(player_health)

# There is no Block Scope in Python
"""
If we create a variable within a function, then it is only available to that particular function.
It is almost like a fence having an apple tree inside and outside

but if you careate a varaible inside an if block, anything outside of the function, then it does not count as scope
they are still accessible
"""
game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy)

# Modifying Global Scope
# Be aware that this makes the code more fallible

enemies = 1

def increase_enemies():
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}") # Output 2

increase_enemies()
print(f"enemies outside function: {enemies}") # Output 2

# what if we want to use that without changing to global scope? we can use return

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}") # Output 1
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}") # Output 1

# Python Constants and Global Scope

# Global Constant - are variables that you defined that never ever planning to changing it again

PI = 3.142 # The naming convention is to turn it in uppercase
URL= "https://"
TWITTER_HANDLE = "@abc"

# So, later on into our code. when we see upper case, we know not to modify it