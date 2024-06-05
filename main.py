## IMPORTS ##
import os
#This is added so we can clear messages in the output.
import time
#This is added to pause the code for the player to read or for the tool's digspeed.
import random
#This is added so we can randomize the chances of getting treasures.
import climage
#This is added so the player can see the item they acquired.
## VARIABLES ##
meters = 0
#This sets the value for how deep the player is.
bbcapacity = 1
#This sets the value for the player's pack.
hcapacity = 0
#Additional storage from helmets
hhcapacity = 1
#Multiply
bcapacity = 0
#Additional storage from bags
wcapacity = 0
wwcapacity = 1
storage = []
#This stores any items the player has dug up which goes to the player's pack.
shoveldamage = 1
#This is the default damage for the player's shovel. It can be upgraded in the shop which increases its damage.
money = 9999999
#The player starts with 0 dollars.
ruby = 99999
#The player starts with 0 rubies.
ground = ""
#This defines the dirt names.
tool = "small"
#The player starts with this pickaxe.
bag = "smallb"
#The player starts with this bag
head = ""
#This is for setting the helmets a string.
waist = ""
shoes = ""
option = 0
#This initializes the option variable.
option2 = 0
#Same thing.
buy = 0
#Same thing.
dirt = 0
#This initializes the dirt's health.
seconds = 0
#This is the speed of your shovel.
nseconds = 0
value = 1
#This will start as one, it will get higher the better tools you get, increases the sell value.
bvalue = 0
#Additional value from bags
bbvalue = 0
#Multiplicative
hvalue = 1
#Additional value from helmets
hhvalue = 1
#Multiplicative
luck = 0
#This will start as zero, it will get higher the better bags you get, increases the odds of finding items.
sbonus = 0
wsbonus = 0
## FUNCTIONS ##
def purge(sec):
  #This is so the screen does not get cluttered with text.
  time.sleep(sec)
  os.system("clear")
## GROUND ##
def define_ground():
  #The ground name will also be changed depending on the depth and for reference to the player.
  global ground
  if meters <= 9:
    ground = "Dirt"
  elif meters >= 10 and meters <= 29:
    ground = "Stone"
  elif meters >= 30 and meters <= 59:
    ground = "Rock"
  elif meters >= 60 and meters <= 89:
    ground = "Granite"
  elif meters >= 90 and meters <= 129:
    ground = "Basalt"
  else:
    ground = "Obsidian"
## DIRT HEALTH ##
def dirt_hp():
  #This is the dirt's health which will be referenced in the dirt_hp() function. 
  global dirt
  if meters <= 9 and dirt <= 0:
    dirt = 1
  elif meters >= 10 and meters <= 29 and dirt <= 0:
    dirt = 5
  elif meters >= 30 and meters <= 59 and dirt <= 0:
    dirt = 10
  elif meters >= 60 and meters <= 89 and dirt <= 0:
    dirt = 25
  elif meters >= 90 and meters <= 129 and dirt <= 0:
    dirt = 50
  elif meters >= 130 and dirt <= 0:
    dirt = 100
## TOOL STATS ##
def tool_stats():
  global tool, shoveldamage, seconds, value
  if tool == "small":
    shoveldamage = 1
    seconds = 2
  elif tool == "regular":
    shoveldamage = 2
    seconds = 1.9
  elif tool == "large":
    shoveldamage = 5
    seconds = 1.85
  elif tool == "bucket":
    shoveldamage = 10
    seconds = 1.8
    value = 1.01
  else:
    quit()
## MAIN ##
def main():
  #This function will be called the most so the game can run in the while loop
  global meters, capacity, storage, money, dirt, option, bvalue, hvalue, value, bcapacity, hcapacity, sbonus, wsbonus
  sbonus = 0
  sbonus += wsbonus
  value = 1
  value = ((((1 + bvalue) + hvalue) * bbvalue) * hhvalue)
  capacity = bcapacity
  capacity = ((((capacity + hcapacity) + wcapacity) * hhcapacity) * bbcapacity)
  print("Depth: " + str(meters) + "m")
  print("Ground Strength: " + ground)
  print("Dirt health: " + str(dirt))
  print("Balance: $" + str(money))
  print("Rubies: ♦️" + str(ruby))
  print("Bag Space: " + str(len(storage)) + "/" + str(capacity))
  print("1. DIG")
  print("2. SELL")
  print("3. STORE")
  print("4. SETTINGS")
  option = int(input("What do you want to do? "))
## STORE ##
def main_store():
  global option2
  purge(0)
  print("1. TOOLS")
  print("2. BAGS")
  print("3. HELMETS")
  print("4. WAIST")
  print("5. SHOES")
  print("6. PADS")
  print("Type any other number to exit")
  option2 = int(input("Where do you want to go? "))
## BAG STORAGE ##
def increase_bag():
  if meters <= 9:
    #Dirt will be added to the storage list which will simulate your capacity.
    storage.append(ground)
  elif meters >= 11 and meters <= 29:
    if tool == "small":
      #If the user has weaker tools like the l pickaxe, then the Rock and higher rank dirts will use a lower number for the range or no for loops.
      storage.append(ground)
    elif tool == "regular" or tool == "large" or tool == "bucket":
      for r in range(5):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
          #Lets say they have a 7/10 bag space, this for loop would only run 3 times because the 4th for loop will have this if statement true which will break and go to the next portion of the code.
  elif meters >= 30 and meters <= 59:
    if tool == "small":
      storage.append(ground)
    elif tool == "regular":
      for r in range(6):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "large":
      for r in range(9):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "bucket":
      for r in range(10):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
  elif meters >= 60 and meters <= 89:
    if tool == "small":
      storage.append(ground)
    elif tool == "regular":
      for r in range(6):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "large":
      for r in range(9):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "bucket":
      for r in range(18):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
  elif meters >= 90 and meters <= 129:
    if tool == "small":
      storage.append(ground)
    elif tool == "regular":
      for r in range(6):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "large":
      for r in range(9):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "bucket":
      for r in range(18):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
  elif meters >= 130:
    if tool == "small":
      storage.append(ground)
    elif tool == "regular":
      for r in range(6):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "large":
      for r in range(9):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
    elif tool == "bucket":
      for r in range(18):
        if len(storage) == capacity:
          break
        else:
          storage.append(ground)
  print("You dug up some " + ground + "!")
## TREASURE ##
def treasure():
  global smallchest, storage, luck, mediumchest, largechest, goldchest, luckychest, meters
  smallchest = random.randint(1, 100 - luck)
  mediumchest = random.randint(1, 200 - luck)
  largechest = random.randint(1, 400 - luck)
  goldchest = random.randint(1, 625 - luck)
  luckychest = random.randint(1, 777 - luck)
  while smallchest <= 1:
    print("You found a Small Chest!")
    print(climage.convert("Treasure/Common.png", is_unicode=True))
    storage.append("Small Chest")
    break
  if meters >= 5:
    while mediumchest <= 1:
      print("You found a Medium Chest!")
      print(climage.convert("Treasure/Rare.png", is_unicode=True))
      storage.append("Medium Chest")
      break
  if meters >= 25:
    while largechest <= 1:
      print("You found a Large Chest!")
      print(climage.convert("Treasure/Epic.png", is_unicode=True))
      storage.append("Large Chest")
      break
  if meters >= 125:
    while goldchest <= 1:
      print("You found a Gold Chest!")
      print(climage.convert("Treasure/Legendary.png", is_unicode=True))
      storage.append("Gold Chest")
      break
  if meters >= 7 and meters <= 777:
    while luckychest <= 1:
      print("You found a Lucky Chest!")
      print(climage.convert("Treasure/Dice_Chest.png", is_unicode=True))
      storage.append("Lucky Chest")
      break
## INTRODUCTION ##
#This is the introduction to my code
print("Welcome. You have found the X Marks the Spot on your treasure map. Before we get started...")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
playername = input("What shall be your name? ")
#Username for the player to choose
print("Alright " + playername + ", you will have a Toy Shovel (Tool), and a Small Bag (Bag).")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Your goal is to mine dirt for valuable items in the ground to acquire stonger tools and bags. If you get deeper in the ground, the dirt will become stronger but the items will become more valuable.")
print("8")
time.sleep(1)
print("7")
time.sleep(1)
print("6")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Good luck " + playername + ", and have fun!")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
purge(0)
main()
## GAMEPLAY ##
while True:
  try:
    while option2 != 4:  
      if option == 1:
        #This checks the length of your storage to see if it's not equal to your max capacity.
        if len(storage) != capacity:
          #dirt_hp() checks how deep you are and sets the dirt health accordingly.
          dirt_hp()
          #tool_stats() checks which tool you have equipped and sets its stats such as speed, damage, and sell value.
          define_ground()
          tool_stats()
          purge(0)
          print("□     □")
          print("□  □  □")
          print("□  □  □")
          purge(seconds)
          print("□     □")
          print("□     □")
          print("□  □  □")
          purge(seconds)
          print("□     □")
          print("□     □")
          print("□     □")
          #This is the dirt's current health.
          dirt = dirt - shoveldamage
          #The meters function adds one every time a dirt block is defeated.
          if dirt > 0:
            meters = meters
          else:
            meters += 1  
          #This adds whatever you dug up into your bag space.
          treasure()
          increase_bag()
          print("2")
          time.sleep(1)
          print("1")
          purge(1)
        else:
          print("Your bag is full!")
          print("3")
          time.sleep(1)
          print("2")
          time.sleep(1)
          print("1")
          time.sleep(1)
          print("Sell your items to buy more space for your bag!")
          print("2")
          time.sleep(1)
          print("1")
          purge(1)
      elif option == 2:
        #X will be the amount of money you got from selling just now.
        x = 0
        #Y will be the amount of rubies you got from selling.
        y = 0
        #The for loop goes through all of the index numbers in the storage list, which would be your bag, and checks what kind of item it is and would give you a value for your money.
        for i in storage:
          if i == "Dirt":
            money += 1 * value
            x += 1 * value
          if i == "Stone":
            money += 2 * value
            x += 2 * value
          if i == "Rock":
            money += 5 * value
            x += 5 * value
          if i == "Granite":
            money += 10 * value
            x += 10 * value
          if i == "Basalt":
            money += 25 * value
            x += 25 * value
          if i == "Obsidian":
            money += 50 * value
            x += 50 * value
          if i == "Small Chest":
            scoins = random.randint(100, 300)
            sruby = random.randint(0, 5)
            money += scoins * value
            ruby += sruby
            x += scoins * value
            y += sruby
          if i == "Medium Chest":
            mcoins = random.randint(500, 1500)
            mruby = random.randint(0, 10)
            money += mcoins * value
            ruby += mruby
            x += mcoins * value
            y += mruby
          if i == "Large Chest":
            lcoins = random.randint(2500, 7500)
            lruby = random.randint(0, 20)
            money += lcoins * value
            ruby += lruby
            x += lcoins * value
            y += lruby
          if i == "Gold Chest":
            gcoins = random.randint(12500, 37500)
            gruby = random.randint(0, 40)
            money += gcoins * value
            ruby += gruby
            x += gcoins * value
            y += gruby
          if i == "Lucky Chest":
            lucoins = random.randint(7, 77777777)
            luruby = random.randint(7, 777)
            money += lucoins * value
            ruby += luruby
            x += lucoins * value
            y += luruby
        money += sbonus * value
        z = sbonus * value
        storage.clear()
        #After that's done, all of the items in the list will be removed so the player can start digging again.
        print("You sold all of your items and gained $" + str(x) + ", and " + str(y) + "♦️, and got a bonus of $" + str(z) + "!")
        print("2")
        time.sleep(1)
        print("1")
        purge(1)
      elif option == 3:
        main_store()
        #This is the shop. The player can input numbers 1-5 to explore the shop.
        if option2 == 1:
          #If the chose 1, they get to pick which tool they want to buy with the number.
          purge(0)
          print("Balance: $" + str(money))
          print("Rubies: ♦️" + str(ruby))
          print("1. Toy Shovel - Free - Damage: 1 Speed: 1.8s")
          print("2. Rake - $800 - Damage: 6 Speed: 1.7s.")
          print("3. Scooper - $2,200 - Damage: 9 Speed: 1.6s.")
          print("4. Bucket - $5,500 - Damage: 18 Speed: 1.8s")
          print("5. Vacuum - $14,000 - Damage: 26 Speed: 1.8s")
          print("Type any other number to exit the shop.")
          buy = int(input("What would you like to buy? "))
          #This portion of the code checks through all of the tools (or until whatever number the user inputted) to see if it's true. If it is true, then the tool will be equipped and will have the applied stats.
          if buy == 1:
            if tool != "small":
              shoveldamage = 1
              seconds = 1.8
              tool = "small"
              print("Equipped the Toy Shovel!")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 2:
            if tool != "regular" and money >= 800:
              money -= 800
              shoveldamage = 6
              seconds = 1.7
              tool = "regular"
              print("Equipped the Rake!")
            elif money < 800:
              print("You don't have enough money for that tool!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 3:
            if tool != "large" and money >= 2200:
              money -= 2200
              shoveldamage = 9
              seconds = 1.6
              tool = "large"
              print("Equipped the Large Toy Shovel")
            elif money < 2200:
              print("You don't have enough money for that tool!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 4:
            if tool != "bucket" and money >= 5500:
              money -= 5500
              shoveldamage = 10
              seconds = 1.8
              tool = "bucket"
              print("Equipped the Bucket!")
            elif money < 5500:
              print("You don't have enough money for that tool!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 5:
            if tool != "vacuum" and money >= 14000:
              money -= 14000
              shoveldamage = 26
              seconds = 1.8
              tool = "vacuum"
              print("Equipped the Vacuum!")
            elif money < 14000:
              print("You don't have enough money for that tool!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          else:
            print("Redirecting you to the main options.")
            print("2")
            time.sleep(1)
            print("1")
        elif option2 == 2:
          purge(0)
          #Basically the same thing from the tools but with bags instead. The user gets to chose which bag they want to buy and will apply its respective stats.
          print("Balance: $" + str(money))
          print("Rubies: ♦️" + str(ruby))
          print("1. Small Bag - Free - Maximum storage is 20.")
          print("2. Medium Bag - $650 - Maximum storage is 75.")
          print("3. Large Bag - $3500 - Maximum Storage is 350.")
          print("4. Travel Backpack - $22,500 - Maximum storage is 1000. - Sell Value x1.3")
          print("Type any other number to exit the shop.")
          buy = int(input("What would you like to buy? "))
          #This portion of the code checks through all of the bag (or until whatever number the user inputted) to see if it's true. If it is true, then the bag will be equipped and will have the applied stats.
          if buy == 1:
            if bag != "smallb":
              bcapacity = 20
              bag = "smallb"
              print("Equipped the Small Bag!")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 2:
            if bag != "mediumb" and money >= 650:
              money -= 650
              bcapacity = 75
              bag = "mediumb"
              print("Equipped the Medium Bag!")
            elif money < 650:
              print("You don't have enough money for that bag!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 3:
            if bag != "largeb" and money >= 5500:
              money -= 5500
              bcapacity = 350
              bag = "largeb"
              print("Equipped the Large Bag!")
            elif money < 5500:
              print("You don't have enough money for that bag!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 4:
            if bag != "travel" and money >= 22500:
              money -= 22500
              bcapacity = 1000
              bag = "travel"
              bvalue = 0.30
              print("Equipped the Travel Backpack!")
            elif money < 22500:
              print("You don't have enough money for that bag!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          else:
            print("Redirecting you to the main options.")
            print("2")
            time.sleep(1)
            print("1")
        elif option == 3:
          purge(0)
          print("Balance: $" + str(money))
          print("Rubies: ♦️" + str(ruby))
          print("1. VR Headset - $77 & 7 Rubies - +77 Bag Storage, +%7 Bag Storage")
          print("2. Helmet - $30,000 & 5 rubies - Sell Value x1.1, +%25 Bag Storage")
          buy = int(input("What would you like to buy? "))
          purge(0)
          #Same stuff but for helmets
          if buy == 1:
            if head != "vr" and money >= 77 and ruby >= 7:
              money -= 77
              ruby -= 7
              hcapacity = 77
              head = "vr"
              hhcapacity = 1.07
              print("Equipped the Helmet!")
            elif money < 77 or ruby < 7:
              print("You don't have enough items for that helmet!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          elif buy == 2:
            if head != "helmet" and money >= 30000 and ruby >= 5:
              money -= 30000
              ruby -= 5
              hhcapacity = 1.25
              head = "helmet"
              hvalue = 0.25
              print("Equipped the Helmet!")
            elif money < 30000 or ruby < 5:
              print("You don't have enough items for that helmet!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
          else:
            print("Redirecting you to the main options.")
            print("2")
            time.sleep(1)
            print("1")
        elif option == 4:
          purge(0)
          print("Balance: $" + str(money))
          print("Rubies: ♦️" + str(ruby))
          print("1. Handbag - $14,000 & 3 Rubies - +500 Bag Storage, +$10 Sell Bonus, +2 Luck")
          buy = int(input("What would you like to buy? "))
          purge(0)
          #Same stuff but for helmets
          if buy == 1:
            if waist != "handbag" and money >= 14000 and ruby >= 3:
              money -= 14000
              ruby -= 3
              wcapacity = 500
              waist = "handbag"
              luck = 3
              wsbonus = 10
              print("Equipped the Handbag!")
            elif money < 14000 or ruby < 3:
              print("You don't have enough items for that waist!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
        elif option == 5:
          purge(0)
          print("Balance: $" + str(money))
          print("Rubies: ♦️" + str(ruby))
          print("1. Sneakers - $4,400 & 1 Ruby - +$2 Sell Bonus, -0.1s Digspeed")
          buy = int(input("What would you like to buy? "))
          purge(0)
          #Same stuff but for helmets
          if buy == 1:
            if shoes != "sneakers" and money >= 4400 and ruby >= 3:
              money -= 4400
              ruby -= 1
              nseconds = 1
              waist = "sneakers"
              ssbonus = 2
              print("Equipped the Handbag!")
            elif money < 4400 or ruby < 1:
              print("You don't have enough items for that waist!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
            else:
              print("You already equipped that item!")
              print("2")
              time.sleep(1)
              print("1")
              time.sleep(1)
              print("Redirecting you to the main options.")
              print("2")
              time.sleep(1)
              print("1")
        purge(1)
      elif option == 4:
        purge(0)
        print("Depth: " + str(meters) + "m")
        print("Ground Strength: " + ground)
        print("Dirt health: " + str(dirt))
        print("Balance: $" + str(money))
        print("Rubies: ♦️" + str(ruby))
        print("Bag Space: " + str(len(storage)) + "/" + str(capacity))
        print("Sell Value: x" + str(value))
        print("Digspeed: " + str(seconds) + "s")
        print("Tool Damage: " + str(shoveldamage))
        print("Luck: +" + str(luck))
        print(storage)
        print("1. LEAVE SETTINGS")
        print("2. QUIT THE GAME")
        option2 = int(input("What do you want to do? "))
        if option2 == 1:
          print("ok")
        if option2 == 2:
          quit()
        purge(0)
      else:
        print("That's not an option.")
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Please try again.")
        print("2")
        time.sleep(1)
        print("1")
        purge(1)
      main()
  except ValueError:
    #If the user inputs anything that's not a number, they would normally get a value error. But with the try-except block, this prevents that from happening, although this is just a placeholder and only brings them to the digsite currently.
    print("Oh no! You've encountered a value error!")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("You typed something that isn't a number which isn't allowed.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Bringing you to the digsite.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
print("Bye bye!")