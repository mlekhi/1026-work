# Developed by: Maya Lekhi
# Date: March 1, 2023
# Desc: a program to allow customers to buy custom build PCs and pre-built PCs based on an existing inventory and checkout their order
# Inputs: category of PC (pre-built or custom build), custom build computer parts, pre-built computer type
# Output: list of price of all PCs in the order

# THINGS TO DO: run test cases

# static inventory list of computer part options for building a PC
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]

# static inventory list of available prebuilt computer options
PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99],['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]

#empty list where price variables will be stored as users indicate what they want to purchase
price = []

print("Welcome to my PC shop!\n")

# defining the Pick Items function; a user-input-driven system for ordering PCs
def pickItems():
    # asking users to choose what PC they want or if they want to finish their order
    pc_type = int(input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? "))
    while pc_type != 3:
        print()
        thisPC = 0
        if pc_type == 1:
            print("Great! Let's start building your PC!\n")

            # listing CPU options that users can select from and adding the cost of it to the total cost of the custom PC
            print("First, let's pick a CPU.")
            for s in CPU:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisCPU = input("Choose the number that corresponds with the part you want: ")
            while not thisCPU.isdigit() or int(thisCPU) not in range(1, len(CPU)+1):
                thisCPU = input("Choose the number that corresponds with the part you want: ")
            thisCPU = int(thisCPU)
            thisPC += float(CPU[thisCPU-1][2])
            print()

            # listing motherboard options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick a compatible motherboard.")
            if thisCPU == 1:
                s = MOTHERBOARD[1]
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
                thisMotherboard = input("Choose the number that corresponds with the part you want: ")
                while not thisMotherboard.isdigit() or int(thisMotherboard) != 2:
                    thisMotherboard = input("Choose the number that corresponds with the part you want: ")
            elif thisCPU == 2:
                s = MOTHERBOARD[0]
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
                thisMotherboard = input("Choose the number that corresponds with the part you want: ")
                while not thisMotherboard.isdigit() or int(thisMotherboard) != 1:
                    thisMotherboard = input("Choose the number that corresponds with the part you want: ")
            else:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
                thisMotherboard = input("Choose the number that corresponds with the part you want: ")
                while not thisMotherboard.isdigit() or int(thisMotherboard) not in range(1, len(MOTHERBOARD) + 1):
                    thisMotherboard = input("Choose the number that corresponds with the part you want: ")
            thisMotherboard = int(thisMotherboard)
            thisPC += float(MOTHERBOARD[thisMotherboard-1][2])
            print()

            # listing RAM options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick your RAM.")
            for s in RAM:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisRAM = input("Choose the number that corresponds with the part you want: ")
            while not thisRAM.isdigit() or int(thisRAM) not in range(1, len(RAM)+1):
                thisRAM = input("Choose the number that corresponds with the part you want: ")
            thisRAM = int(thisRAM)
            thisPC += float(RAM[thisRAM-1][2])
            print()

            # listing PSU options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick your PSU.")
            for s in PSU:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisPSU = input("Choose the number that corresponds with the part you want: ")
            while not thisPSU.isdigit() or int(thisPSU) not in range(1, len(PSU)+1):
                thisPSU = input("Choose the number that corresponds with the part you want: ")
            thisPSU = int(thisPSU)
            thisPC += float(PSU[thisPSU-1][2])
            print()

            # listing case options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick your case.")
            for s in CASE:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisCase = input("Choose the number that corresponds with the part you want: ")
            while not thisCase.isdigit() or int(thisCase) not in range(1, len(CASE)+1):
                thisCase = input("Choose the number that corresponds with the part you want: ")
            thisCase = int(thisCase)
            thisPC += float(CASE[thisCase-1][2])
            print()

            # listing SSD options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
            for s in SSD:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisSSD = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
            while not (thisSSD.isdigit() and int(thisSSD) in range(1, len(SSD) + 1) or thisSSD.lower() == 'x'):
                thisSSD = input("Choose the number that corresponds with the part you want (or X to not get an SSD): ")
            if thisSSD.lower() != 'x':
                thisPC += float(SSD[int(thisSSD) - 1][2])
            print()

            # listing HDD options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
            for s in HDD:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            if thisSSD.lower() == 'x':
                thisHDD = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
                while not thisHDD.isdigit() or int(thisHDD) not in range(1, len(HDD) + 1):
                    thisHDD = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD): ")
            else:
                thisHDD = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
                while not (thisHDD.isdigit() and int(thisHDD) in range(1, len(HDD) + 1) or thisHDD.lower() == 'x'):
                    thisHDD = input("Choose the number that corresponds with the part you want (or X to not get an HDD): ")
            if thisHDD.lower() != 'x':
                thisPC += float(HDD[int(thisHDD) - 1][2])
            print()

            # listing graphics card options that users can select from and adding the cost of it to the total cost of the custom PC
            print("Finally, let's pick your graphics card (or X not to get a graphics card).")
            for s in GRAPHICS_CARD:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisGraphicsCard = input("Choose the number that corresponds with the part you want: ")
            while not (thisGraphicsCard.isdigit() and int(thisGraphicsCard) in range(1, len(GRAPHICS_CARD) + 1) or thisGraphicsCard.lower() == 'x'):
                thisGraphicsCard = input("Choose the number that corresponds with the part you want: ")
            if thisGraphicsCard.lower() != 'x':
                thisPC += float(GRAPHICS_CARD[int(thisGraphicsCard) - 1][2])
            print()

            # adding the total price of this PC to the price list to be displayed at the end of when the function is called
            price.append(round(thisPC,2))

            # displaying price of prebuilt PC and resetting the individual PC price variable
            print("You have selected all the required parts! Your total for this PC is ${}".format(round(thisPC,2)))
            thisPC = 0
            print()

        elif pc_type == 2:
            print("Great! Let's pick a pre-built PC!")
            print()

            # listing prebuilt options that users can select from and adding the cost
            for s in PREBUILTS:
                print(f"{s[0]}: {s[1]}, ${s[2]:.2f}")
            thisPrebuilt = input("Choose the number that corresponds with the part you want: ")
            while not (thisPrebuilt.isdigit() and int(thisPrebuilt) in range(1, len(PREBUILTS) + 1)):
                thisPrebuilt = input("Choose the number that corresponds with the part you want: ")
            thisPrebuilt = int(thisPrebuilt)
            thisPC += float(PREBUILTS[thisPrebuilt-1][2])

            # adding the total price of this PC to the price list to be displayed at the end of when the function is called
            price.append(round(thisPC,2))
            print()

            # displaying price of prebuilt PC and resetting the individual PC price variable
            print("Your total price for this prebuilt is ${}".format(round(thisPC,2)))
            thisPC = 0
            print()

        # asking users to choose what PC they want or if they want to finish their order
        pc_type = int(input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? "))

    # when the function is called, it will print the individual PC prices stored in the "price"  variable
    print(price)

pickItems()
