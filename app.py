minion = input("Which minion would you like to check? ")
level = input("Which tier " + minion + " minion" + " are you checking? ")
#speed = input("What is your minion's speed? (second/block) ")
cost = input("What is the sell price of " + minion + " at the bazzar? ")
if minion == "Cobblestone":
    levelArray = [14, 14, 12, 12, 10, 10, 9, 9, 8, 8, 7]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Coal":
    levelArray = [15, 15, 13, 13, 12, 12, 10, 10, 9, 9, 7]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Glowstone":
    levelArray = [25, 25, 23, 23, 21, 21, 19, 19, 16, 16, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Gravel":
    levelArray = [26, 26, 24, 24, 22, 22, 19, 19, 16, 16,13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Obsidian":
    levelArray = [45, 45, 42, 42, 39, 39, 35, 35, 30, 30, 24]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Sand":
    levelArray = [26, 26, 24, 24, 22, 22, 19, 19, 16, 16, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Clay":
    levelArray = [32, 32, 30, 30, 27.5, 27.5, 24, 24, 20, 20, 16]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Ice":
    levelArray = [14, 14, 12, 12, 10, 10, 9, 9, 8, 8, 7]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Snow":
    levelArray = [13, 13, 12, 12, 11, 11, 9.5, 9.5, 8, 8, 6.5]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Iron":
    levelArray = [17, 17, 15, 15, 14, 14, 12, 12, 10, 10, 8]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Gold":
    levelArray = [22, 22, 20, 20, 18, 18, 16, 16, 14, 14, 11]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Diamond":
    levelArray = [29, 29, 27, 27, 25, 25, 22, 22, 19, 19, 15]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Lapis":
    levelArray = [29, 29, 27, 27, 25, 25, 23, 23, 21, 21, 18]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Redstone":
    levelArray = [29, 29, 27, 27, 25, 25, 23, 23, 21, 21, 18]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Emerald":
    levelArray = [28, 28, 26, 26, 24, 24, 21, 21, 18, 18, 14]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Quartz":
    levelArray = [22.5, 22.5, 21, 21, 19, 19, 17, 17, 14.5, 14.5, 11.5]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "End Stone":
    levelArray = [26, 26, 24, 24, 22, 22, 19, 19, 16, 16, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Wheat":
    levelArray = [15, 15, 13, 13, 11, 11, 10, 10, 9, 9, 8]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Melon":
    levelArray = [24, 24, 22.5, 22.5, 21, 21, 18.5, 18.5, 16, 16, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Pumpkin":
    levelArray = [32, 32, 30, 30, 27, 27, 24, 24, 20, 20, 16]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Carrot":
    levelArray = [20, 20, 18, 18, 16, 16, 14, 14, 12, 12, 10]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Potato":
    levelArray = [20, 20, 18, 18, 16, 16, 14, 14, 12, 12, 10]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Mushroom":
    levelArray = [30, 30, 28, 28, 26, 26, 23, 23, 20, 20, 16]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Cactus":
    levelArray = [27, 27, 25, 25, 23, 23, 21, 21, 18, 18, 15]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Cocoa Beans":
    levelArray = [27, 27, 25, 25, 23, 23, 21, 21, 18, 18, 15]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Suger Cane":
    levelArray = [22, 22, 20, 20, 18, 18, 16, 16, 14.5, 14.5, 12]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Nether Wart":
    levelArray = [50, 50, 47, 47, 44, 44, 41, 41, 38, 38, 32]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Flower":
    levelArray = [30, 29, 28, 27, 26, 25, 24, 23, 22, 20, 18]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Fishing":
    levelArray = [78, 75, 72, 72, 68, 68, 62.5, 62.5, 53, 53, 35]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Zombie":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Revenant":
    levelArray = [29, 29, 26, 26, 23, 23, 19, 19, 14.5, 14.5, 10]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Skeleton":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Creeper":
    levelArray = [27, 27, 25, 25, 23, 23, 21, 21, 18, 18, 14]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Spider":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Tarantula":
    levelArray = [29, 29, 26, 26, 23, 23, 19, 19, 14.5, 14.5, 10]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Cave Spider":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Blaze":
    levelArray = [33, 33, 31, 31, 28.5, 28.5, 25, 2521, 21, 16.5]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Magma Cube":
    levelArray = [32, 32, 30, 30, 28, 28, 25, 25, 22, 22, 18]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Enderman":
    levelArray = [32, 32, 30, 30, 28, 28, 25, 25, 22, 22, 18]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Ghast":
    levelArray = [50, 50, 47, 47, 44, 44, 41, 41, 38, 38, 32]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Slime":
    levelArray = [26, 26, 24, 24, 22, 22, 19, 19, 16, 16, 12]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Cow":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Pig":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17,13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Chicken":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 18, 18, 15]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Sheep":
    levelArray = [24, 24, 22, 22, 20, 20, 18, 18, 16, 16, 12]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Rabbit":
    levelArray = [26, 26, 24, 24, 22, 22, 20, 20, 17, 17, 13]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Oak":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Spruce":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Birch":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Dark Oak":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Acia":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
if minion == "Jungle":
    levelArray = [48, 48, 45, 45, 42, 42, 38, 38, 33, 33, 27]
    value = round(3600 / levelArray[int(level)] * float(cost))
    coins: str = "{} coins per hour.".format(value)
    print(coins)
