

import random

def generateDistances(current, target):
    global _0to1, _0to3, _1to2, _1to4, _2to4, _3to4
    distances = []
    routes = ["Route 1", "Route 2", "Route 3", "Route 4"]
    locations = ["Holy City", "Deep Forest", "Cursed Village", "Watcher's Outpost", "Gateway to Hell"]
    current = str(current)
    if current == "0": #Holy City as current
        if target == "0":
            print("You're already here.")
        elif target == "1":
            #Deep Forest
            distances.append(_0to1)
            distances.append(_0to3 + _3to4 + _1to4)
            distances.append(_0to3 + _3to4 + _2to4 + _1to2)
            print(f"Route 1: {locations[0]} to {locations[1]}\nRoute 2: {locations[0]} to {locations[3]} to {locations[4]} to {locations[1]}\nRoute 3: {locations[0]} to {locations[3]} to {locations[4]} to {locations[2]} to {locations[1]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "2":
            #Cursed Village
            distances.append(_0to1 + _1to2)
            distances.append(_0to3 + _3to4 + _1to4 + _1to2)
            distances.append(_0to3 + _3to4 + _2to4)
            distances.append(_0to1 + _1to4 + _2to4)
            print(f"Route 1: {locations[0]} to {locations[1]} to {locations[2]}\nRoute 2: {locations[0]} to {locations[3]} to {locations[4]} to {locations[1]} to {locations[2]}\nRoute 3: {locations[0]} to {locations[3]} to {locations[4]} to {locations[2]}\nRoute 4: {locations[0]} to {locations[1]} to {locations[4]} to {locations[2]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "3":
            #Watcher's Tower
            distances.append(_0to1 + _1to4 + _3to4)
            distances.append(_0to1 + _1to2 + _2to4 + _3to4)
            distances.append(_0to3)
            print(f"Route 1: {locations[0]} to {locations[1]} to {locations[4]} to {locations[3]}\nRoute 2: {locations[0]} to {locations[1]} to {locations[2]} to {locations[4]} to {locations[3]}\nRoute 3: {locations[0]} to {locations[3]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "4":
            #Gateway of Hell
            distances.append(_0to1 + _1to4)
            distances.append(_0to3 + _3to4)
            distances.append(_0to1 + _1to2 + _2to4)
            print(f"Route 1: {locations[0]} to {locations[1]} to {locations[4]}\nRoute 2: {locations[0]} to {locations[3]} to {locations[4]}\nRoute 3: {locations[0]} to {locations[1]} to {locations[2]} to {locations[4]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        else: print("Unknown Location.")
    elif current == "1": #Deep Fores as current
        if target == "1":
            print("You're already here.")
        elif target == "0":
            #Holy City
            distances.append(_0to1)
            distances.append(_1to2 + _2to4 + _3to4 + _0to3)
            distances.append(_1to4 + _3to4 + _0to3)
            print(f"Route 1: {locations[1]} to {locations[0]}\nRoute 2: {locations[1]} to {locations[2]} to {locations[4]} to {locations[3]} to {locations[0]}\nRoute 3: {locations[1]} to {locations[4]} to {locations[3]} to {locations[0]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "2":
            #Cursed Village
            distances.append(_1to2)
            distances.append(_1to4 + _2to4)
            distances.append(_0to1 + _0to3 + _3to4 + _2to4)
            distances.append(_0to1 + _0to3 + _3to4 + _1to4 + _1to2)
            print(f"Route 1: {locations[1]} to {locations[2]}\nRoute 2: {locations[1]} to {locations[4]} to {locations[2]}\nRoute 3: {locations[1]} to {locations[0]} to {locations[3]} to {locations[4]} to {locations[2]}\nRoute 4: {locations[1]} to {locations[0]} to {locations[3]} to {locations[4]} to {locations[1]} to {locations[2]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "3":
            #Watcher's Tower
            distances.append(_1to2 + _2to4 + _3to4)
            distances.append(_1to4 + _3to4)
            distances.append(_0to1 + _0to3)
            print(f"Route 1: {locations[1]} to {locations[2]} to {locations[4]} to {locations[3]}\nRoute 2: {locations[1]} to {locations[4]} to {locations[3]}\nRoute 3: {locations[1]} to {locations[0]} to {locations[3]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "4":
            #Gateway of Hell
            distances.append(_1to4)
            distances.append(_1to2 + _2to4)
            distances.append(_0to1 + _0to3 + _3to4)
            print(f"Route 1: {locations[1]} to {locations[4]}\nRoute 2: {locations[1]} to {locations[2]} to {locations[4]}\nRoute 3: {locations[1]} to {locations[0]} to {locations[3]} to {locations[4]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        else: print("Unknown Location.")
    elif current == "2": #Cursed Village as current
        if target == "2":
            print("You're already here.")
        elif target == "0":
            #Holy City
            distances.append(_1to2 + _0to1)
            distances.append(_2to4 + _3to4 + _0to3)
            distances.append(_1to2 + _1to4 + _3to4 + _0to3)
            distances.append(_2to4 + _1to4 + _0to1)
            print(f"Route 1: {locations[2]} to {locations[1]} to {locations[0]}\nRoute 2: {locations[2]} to {locations[4]} to {locations[3]} to {locations[0]}\nRoute 3: {locations[2]} to {locations[1]} to {locations[4]} to {locations[3]} to {locations[0]}\nRoute 4: {locations[2]} to {locations[4]} to {locations[1]} to {locations[0]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "1":
            #Deep Forest
            distances.append(_2to4 + _1to4)
            distances.append(_1to2)
            distances.append(_2to4 + _3to4 + _0to3 + _0to1)
            print(f"Route 1: {locations[2]} to {locations[4]} to {locations[1]}\nRoute 2: {locations[2]} to {locations[1]}\nRoute 3: {locations[2]} to {locations[4]} to {locations[3]} to {locations[0]} to {locations[1]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "3":
            #Watcher's Tower
            distances.append(_2to4 + _1to4 + _0to1 + _0to3)
            distances.append(_1to2 + _1to4 + _3to4)
            distances.append(_2to4 + _3to4)
            print(f"Route 1: {locations[2]} to {locations[4]} to {locations[1]} to {locations[0]} to {locations[3]}\nRoute 2: {locations[2]} to {locations[1]} to {locations[4]} to {locations[3]}\nRoute 3: {locations[2]} to {locations[4]} to {locations[3]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "4":
            #Gateway of Hell
            distances.append(_2to4)
            distances.append(_1to2 + _2to4)
            distances.append(_1to2 + _0to1 + _0to3 + _3to4)
            print(f"Route 1: {locations[2]} to {locations[4]}\nRoute 2: {locations[2]} to {locations[1]} to {locations[4]}\nRoute 3: {locations[2]} to {locations[1]} to {locations[0]} to {locations[3]} to {locations[4]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        else: print("Unknown Location.")
    elif current == "3": #Watcher's Outpost as current
        if target == "3":
            print("You're already here.")
        elif target == "0":
            #Holy City
            distances.append(_0to3)
            distances.append(_3to4 + _1to4 + _0to1)
            distances.append(_3to4 + _2to4 + _1to2 + _0to1)
            print(f"Route 1: {locations[3]} to {locations[0]}\nRoute 2: {locations[3]} to {locations[4]} to {locations[1]} to {locations[0]}\nRoute 3: {locations[3]} to {locations[4]} to {locations[2]} to {locations[1]} to {locations[0]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "1":
            #Deep Forest
            distances.append(_0to3 + _0to1)
            distances.append(_3to4 + _1to4)
            distances.append(_3to4 + _2to4 + _1to2)
            print(f"Route 1: {locations[3]} to {locations[0]} to {locations[1]}\nRoute 2: {locations[3]} to {locations[4]} to {locations[1]}\nRoute 3: {locations[3]} to {locations[4]} to {locations[2]} to {locations[1]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "2":
            #Cursed Village
            distances.append(_0to3 + _0to1 + _1to2)
            distances.append(_3to4 + _1to4 + _1to2)
            distances.append(_3to4 + _2to4)
            print(f"Route 1: {locations[3]} to {locations[0]} to {locations[1]} to {locations[2]}\nRoute 2: {locations[3]} to {locations[4]} to {locations[1]} to {locations[2]}\nRoute 3: {locations[3]} to {locations[4]} to {locations[2]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "4":
            #Gateway of Hell
            distances.append(_0to3 + _0to1 + _1to4)
            distances.append(_3to4)
            distances.append(_0to3 + _0to1 + _1to2 + _2to4)
            print(f"Route 1: {locations[3]} to {locations[0]} to {locations[1]} to {locations[4]}\nRoute 2: {locations[3]} to {locations[4]}\nRoute 3: {locations[3]} to {locations[0]} to {locations[1]} to {locations[2]} to {locations[4]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        else: print("Unknown Location.")
    elif current == "4": #Gateway of Hell as current
        if target == "4":
            print("You're already here.")
        elif target == "0":
            #Holy City
            distances.append(_3to4 + _0to3)
            distances.append(_1to4 + _0to1)
            distances.append(_2to4 + _1to2 + _0to1)
            print(f"Route 1: {locations[4]} to {locations[3]} to {locations[0]}\nRoute 2: {locations[4]} to {locations[1]} to {locations[0]}\nRoute 3: {locations[4]} to {locations[2]} to {locations[1]} to {locations[0]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "1":
            #Deep Forest
            distances.append(_1to4)
            distances.append(_2to4 + _1to2)
            distances.append(_3to4 + _0to3 + _0to1)
            print(f"Route 1: {locations[4]} to {locations[1]}\nRoute 2: {locations[4]} to {locations[2]} to {locations[1]}\nRoute 3: {locations[4]} to {locations[3]} to {locations[0]} to {locations[1]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "2":
            #Cursed Village
            distances.append(_2to4)
            distances.append(_1to4 + _1to2)
            distances.append(_3to4 + _0to3 + _0to1 + _1to2)
            print(f"Route 1: {locations[4]} to {locations[2]}\nRoute 2: {locations[4]} to {locations[1]} to {locations[2]}\nRoute 3: {locations[4]} to {locations[3]} to {locations[0]} to {locations[1]} to {locations[2]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        elif target == "3":
            #Watcher's Tower
            distances.append(_1to4 + _0to1 + _0to3)
            distances.append(_3to4)
            distances.append(_2to4 + _1to2 + _0to1 + _0to3)
            print(f"Route 1: {locations[4]} to {locations[1]} to {locations[0]} to {locations[3]}\nRoute 2: {locations[4]} to {locations[3]}\nRoute 3: {locations[4]} to {locations[2]} to {locations[1]} to {locations[0]} to {locations[3]}\n\nDistances:")
            for i in range(0, len(distances)):
                print(f"{routes[i]}: {distances[i]}m - Arrival Time: {int((distances[i] / .1)/60)}min")

            print(f"Recommend Route: {routes[distances.index(min(distances))]}")
        else: print("Unknown Location.")


def GenerateMap():
    generateLocation = random.randint(0, 4)
    mapping = r'''
        |=====|             ==            ==                     |===|         |===|
        |     |            ====    ==    ====                  |=======|  /\ |=======|
        |     | <=======>   ||    ====    ||    ==   <=======>   |===|   |==|  |===|
        |     |                    ||          ====              |===|   |==|  |===|
        |=====|                                 ||
       Holy City                 Deep Forest                        Cursed Village
           0                          1          \|\                       2
          /\                                       \|\                     /\
          ||                                         \|\                   ||
          \/                                           \|\                 \/
                                                         \|\
        || || ||                                           \|\      ||==========||
         ++++++                                              \|\   ||            ||
         ||  ||                                                   ||              ||
         ||  || <=============================================>  ||                ||
         ||  ||                                                  ||                ||
         ======                                                  ||================||
    Watcher's Outpost                                               Gateway to Hell
            3                                                              4

    Legend:
        ! - Current Location
        0 to 4 - Area number.
           '''

    mapping = mapping.replace(str(generateLocation), "!")

    print(mapping)
    #Ask the user where he would want to go
    print('''
        Where do you want to go?

        0 - Holy City
        1 - Deep Forest
        2 - Cursed Village
        3 - Watcher's Outpost
        4 - Gateway to Hell
        ''')
    query = input("Destination: ")
    generateDistances(generateLocation, query)

    #Add the missing conditions
    #Polish the data


#Map Variable
_0to1 = random.randint(10, 100)
_0to3 = random.randint(10, 100)
_1to2 = random.randint(10, 100)
_1to4 = random.randint(10, 100)
_2to4 = random.randint(10, 100)
_3to4 = random.randint(10, 100)



GenerateMap()


