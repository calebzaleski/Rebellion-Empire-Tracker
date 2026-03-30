import sqlite3

connected = sqlite3.connect('data/main.db')
cursor = connected.cursor()

#[(0, 'id', 'INTEGER', 0, None, 1),
# (1, 'name', 'TEXT', 1, None, 0),
# (2, 'probe_card', 'BOOLEAN', 0, None, 0),
# (3, 'occupied', 'BOOLEAN', 0, None, 0),
# (4, 'loyalty', 'TEXT', 0, None, 0),
# (5, 'region', 'TEXT', 1, "'unknown'", 0)]

selection = ""
update_var = ""
update_planet = ""
def create_DB():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL DEFAULT 'name me plz',
    probe_card BOOL NOT NULL DEFAULT 0,
    occupied BOOL NOT NULL DEFAULT 0,
    loyalty TEXT NOT NULL DEFAULT 'Neutral',
    region TEXT NOT NULL DEFAULT 'give me a region plz'
    );
""")
def drop_DB():
    cursor.execute("""drop table if exists system""")
def load_DB():
    cursor.execute("""
        INSERT INTO system (name, region)
        VALUES
        ('Mon Calamari', 'Top Left'),
        ('Yavin', 'Top Left'),
        ('Saleucami', 'Top Left'),
        ('Felucia', 'Top Left'),
        ('Kessel', 'Top Middle'),
        ('Nal Hutta', 'Top Middle'),
        ('Toydaria', 'Top Middle'),
        ('Bothawui', 'Top Middle'),
        ('Tatooine', 'Top Right'),
        ('Rodia', 'Top Right'),
        ('Geonosis', 'Top Right'),
        ('Ryloth', 'Top Right'),
        ('Dathomir', 'Middle'),
        ('Mandalore', 'Middle'),
        ('Kashyyk', 'Middle'),
        ('Malastare', 'Middle'),
        ('Naboo', 'Middle Right'),
        ('Sullust', 'Middle Right'),
        ('Dagobah', 'Middle Right'),
        ('Utapau', 'Middle Right'),
        ('Mustafar', 'Bottom Right'),
        ('Hoth', 'Bottom Right'),
        ('Endor', 'Bottom Right'),
        ('Corellia', 'Bottom Right'),
        ('Bespin', 'Bottom Right'),
        ('Corusant', 'Bottom Middle'),
        ('Corellia', 'Bottom Middle'),
        ('Cato Neimodia', 'Bottom Middle'),
        ('Alderaan', 'Bottom Middle'),
        ('Dantoine', 'Bottom Left'),
        ('Mygeeto', 'Bottom Left'),
        ('Ilum', 'Bottom Left'),
        ('Ord Mantell', 'Bottom Left');    
                   """)


def showone(selection):
        cursor.execute("SELECT * FROM system WHERE lower(name) = lower(?)", (selection,))

        planet = cursor.fetchone()

        system = "\033[92m"+planet[1]+"\033[0m"

        region = "\033[92m"+planet[5]+"\033[0m"

        if planet[3] == 1:
                occupied = "You \033[92mhave\033[0m ground troops"
        else:
                occupied = "You have \033[91mno\033[0m ground troops"


        if planet[2] == 1:
                probe = "and you \033[92mhave\033[0m a probe card"
        else:
                probe = "and you do \033[91mnot\033[0m have a probe card"

        if planet is None:
                print("Error")
                return

        print("Status of:", system, "in the",region , "region.", occupied, probe)
def showall():
    cursor.execute("SELECT name, probe_card, occupied, loyalty, region FROM system")
    rows = cursor.fetchall()

    header = f"{'Name':^26}{'Probe':^26} {'Troop':^26}{'Loyalty':^26}{'Region':^26}{'Base':^26}"
    print(header)
    print("|", "-" * 72, "|", "-" * 73, "|")

    for i in range(0,31,2):
        left = rows[i]

        if left[1] == 1 or left[2] == 1:
            base_text = f"{'Not the base':^18}"
            Base = f"\033[92m{base_text}\033[0m"
        else:
            base_text = f"{'Unknown ATM':^18}"
            Base = f"\033[91m{base_text}\033[0m"

        if left[1] == 1:
            probe = "\033[92m✓\033[0m"
        else:
            probe = "\033[91m✗\033[0m"

        if left[2] == 1:
            troop = "\033[92m✓\033[0m"
        else:
            troop = "\033[91m✗\033[0m"


        left_text = f"{left[0]:^18}{probe:^5} {troop:^5}{left[3]:^15}{left[4]:^18}\033[91m{Base:^18}"

        if i + 1 < len(rows):
            right = rows[i + 1]

            if right[1] == 1 or right[2] == 1:
                base_text = f"{'Not the base':^18}"
                Base = f"\033[92m{base_text}\033[0m"
            else:
                base_text = f"{'Unknown ATM':^18}"
                Base = f"\033[91m{base_text}\033[0m"

            if right[1] == 1:
                probe = "\033[92m✓\033[0m"
            else:
                probe = "\033[91m✗\033[0m"

            if right[2] == 1:
                troop = "\033[92m✓\033[0m"
            else:
                troop = "\033[91m✗\033[0m"



            right_text = f"{right[0]:^18}{probe:^5} {troop:^5}{right[3]:^15}{right[4]:^18}{Base:^18}"
            print(f"| {left_text} |  {right_text} |")
    print("|", "-" * 72, "|", "-" * 73, "|")


def updateplanet(update_var, update_planet):
    if update_var == "1":
            cursor.execute("update system set probe_card = 1 - probe_card where lower(name) = lower(?)", (update_planet,))
            print("Probe card updated")

    elif update_var == "2":
        cursor.execute("update system set occupied = 1 - occupied where lower(name) = lower(?)", (update_planet,))
        print("Occupied card updated")

    elif update_var == "3":
        print("Set to:\n 1. Rebel \n 2. Subjugated \n 3. Imperial")
        loytaly = input()
        if loytaly == "1":
            cursor.execute("update system set loyalty ='Rebel' where lower(name) = lower(?)", (update_planet,))
        elif loytaly == "2":
            cursor.execute("update system set loyalty ='Subjugated' where lower(name) = lower(?)", (update_planet,))
        elif loytaly == "3":
            cursor.execute("update system set loyalty ='Imperial' where lower(name) = lower(?)", (update_planet,))

        print("Loyalty card updated")


#--------START MAIN USER INTERACTION----------#

print("\nCurrent status: \n")
showall()
print("\nHello there, would you like to:")

while 1 == 1:
        print(" 1. List planet Status")
        print(" 2. Update Planet")
        print(" 3. Show all Planet")
        print(" 4. Save")
        print(" 5. Reset")


        userinput = input()

        if userinput == "1":
            print("Which planet?")
            planet = input()
            showone(planet)

        elif userinput == "2":
            print("Which would you like to update: \n 1. Probe Card \n 2. Occupied \n 3. Loyalty")
            update_var = input()
            print("Which planets would you like to update? (comma separated)")
            planets_input = input()

            planets = [planet.strip() for planet in planets_input.split(",") if planet.strip()]

            for update_planet in planets:
                updateplanet(update_var, update_planet)


        elif userinput == "3":
            showall()

        elif userinput == "4":
            print("goodbye")
            connected.commit()
            connected.close()
            break

        elif userinput == "5":
            print("Type 'reset' to confirm:")
            userinput = input()
            if str(userinput).lower() == "reset":
                drop_DB()
                create_DB()
                load_DB()
                print("Program Reset")
            else:
                print("Failed")

#--------END MAIN USER INTERACTION----------#




