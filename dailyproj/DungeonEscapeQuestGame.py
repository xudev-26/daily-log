import os
import random
from datetime import datetime

#===========================FILENAMES========================================
files = {#dictionary of text files that acts as a storages!
    "accounts": "account.txt",
    "enemies": "enemies.txt",
    "items": "items.txt",
    "rooms": "rooms.txt",
    "questions": "questions.txt",
    "player_progress": "player_progress.txt",
    "battle_history": "battle_history.txt",
    "enemy_difficulty": "enemy_difficulty.txt",
    "starting_items": "starting_items.txt",
    "starting_enemies": "starting_enemies.txt",
    "defeated_enemies": "defeated_enemies.txt",
    "boss_status": "boss_status.txt",

}

#=======================UTILITY FUNCTIONS====================================

def ensure_file_exists(filename, default_content=""):
    """a function that takes two argument, but one is defeault. this function
    ensure the files exists, if not then create a files for it"""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(default_content)

            
def read_file_lines(filename):
    """function that takes one arg, job is to read the files,
    but first making sure that files exists in the first place. this function
    returns a list of string"""
    ensure_file_exists(filename)
    with open(filename, "r") as f:
        return[line.strip() for line in f if line.strip()]


def write_file_lines(filename, lines):
    """the job of this function is to open the files in write mode,
    then iterates through the param lines and add a newline"""
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def append_to_file(filename, line):
    """this opens the file in append mode, then evaluate if the file exist.
    Then check if the byte size of the files is greater than zero, if both are True,
    then open the filename or path again in readbyte mode as existing files.
    then start at the end and read backwards. then evaluate the existing file if
    the first letter isnt equal to bytes newline, if so then write a newline in it.
    after all is done, concatenate the line param to newline"""
    with open(filename, "a") as f:
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open(filename, "rb") as existing_file:
                existing_file.seek(-1, os.SEEK_END)
                if existing_file.read(1) != b"\n":
                    f.write("\n")
        f.write(line + "\n")

def parse_record(line, delimiter="|"):
    """this function has two arg, one is defult. this function returns
    a list of string"""
    return [field.strip() for field in line.split(delimiter)]

def format_record(fields, delimiter="|"):
    """this returns a joins list of string together"""
    return delimiter.join(str(f) for f in fields)

def generate_id(existing_ids):
    """this function's job is to generate an id, this returns a string
    a string of highest number, then if there is no id's found.
    it will default into 0"""
    numeric_ids = [int(i) for i in existing_ids if i.isdigit()] #a list comp that iterates through the param
    #it check if the param is an actual number, if so then convert it into an integer
    return str(max(numeric_ids, default=0) + 1)

def get_existing_ids(filename):
    """this function job is to get the id's,
    it iterates through the read_file_lines 
    and for every iteration it gets passed into 
    parse record, then if true. it will append the parts into 
    empty list of ids, then return that ids"""
    lines = read_file_lines(filename)
    ids = []
    for line in lines:
        parts = parse_record(line)
        if parts:
            ids.append(parts[0])
        
    return ids

def find_record_by_id(filename, record_id):
    """this takes two arg, which is for filename and record id,
    the job of this function is to index the filename and parse it,
    if the first index is equal to record id, then return the index and
    also the parts. if nothing is found, then return -1 and None"""
    lines = read_file_lines(filename)
    for i, line in enumerate(lines):
        parts = parse_record(line)
        if parts and parts[0] == str(record_id):
            return i, parts 
    return -1, None 

def clear_screen():
    """Just for clearing the screen everytime, 
    aesthetic purposes i guess"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """For header design"""
    print('=' * 60)
    print(f'  {title:^56}')
    print('=' * 60)

def pause():
    """Ofc for pausing the game"""
    input("Press Enter to continue...")

#=============================INITILLIZATION===========================

def initialize_system():
    """now the purpose of this function is to give data files, and
    if they didnt exists, because of ensure func, they will be created"""
    ensure_file_exists(files["accounts"], 
        "1|admin|admin123|Admin|Game Administrator\n"
        "2|player1|player123|Player|Knight Player\n"
        "3|player2|player123|Player|Mage Player\n"
        "4|player3|player123|Player|Archer Player\n"
        "5|player4|player123|Player|Warrior Player\n"
        "6|player5|player123|Player|Rogue Player"
    )

    ensure_file_exists(files["enemies"],
        "1|Dungeon Goblin|20|5|10|50|No|Easy\n"
        "2|Skeleton Warrior|35|8|15|75|No|Easy\n"
        "3|Dark Spider|30|10|20|100|No|Medium\n"
        "4|Orc Berserker|50|12|25|150|No|Medium\n"
        "5|Shadow Knight|60|15|30|200|No|Hard\n"
        "6|Dragon Lord|100|20|50|500|Yes|Hard"
    )

    ensure_file_exists(files["items"],
        "1|Health Potion|Heal|30|Restores 30 HP\n"
        "2|Greater Health Potion|Heal|60|Restores 60 HP\n"
        "3|Strength Elixir|Buff|5|Increases attack by 5\n"
        "4|Iron Shield|Defense|10|Reduces damage by 10\n"
        "5|Magic Ring|Buff|8|Increases attack by 8\n"
        "6|Revive Token|Special|50|Revives with 50 HP"
    )

    ensure_file_exists(files["rooms"],
        "1|Entrance Hall|A dark and dusty entrance|5|Yes|Yes\n"
        "2|Treasure Chamber|Glittering gold everywhere|0|Yes|Yes\n"
        "3|Spider Den|Cobwebs cover the walls|10|Yes|No\n"
        "4|Orc Barracks|Smells of battle and blood|8|Yes|Yes\n"
        "5|Shadow Corridor|Whispers echo in the dark|12|Yes|No\n"
        "6|Dragon Lair|The final challenge awaits|15|Yes|Yes"
    )

    ensure_file_exists(files["questions"],
        "1|What is 2+2?|3|4|5|6|B\n"
        "2|Capital of France?|London|Berlin|Paris|Madrid|C\n"
        "3|Largest planet?|Earth|Mars|Jupiter|Venus|C\n"
        "4|5 x 6 = ?|25|30|35|40|B\n"
        "5|Who painted the Mona Lisa?|Van Gogh|Picasso|Da Vinci|Rembrandt|C\n"
        "6|What is the speed of light?|300000 km/s|150000 km/s|100000 km/s|500000 km/s|A"
    )

    ensure_file_exists(files["player_progress"],
        "2|Knight Player|100|100|10|2|0|0|1|No\n"
        "3|Mage Player|80|80|15|3|0|0|1|No\n"
        "4|Archer Player|90|90|12|2|0|0|1|No\n"
        "5|Warrior Player|120|120|8|1|0|0|1|No\n"
        "6|Rogue Player|85|85|14|2|0|0|1|No"
    )

    ensure_file_exists(files["battle_history"],
        "1|2|Knight Player|1|Dungeon Goblin|Win|2026-08-15|10|50\n"
        "2|3|Mage Player|2|Skeleton Warrior|Loss|2026-08-15|0|0\n"
        "3|4|Archer Player|1|Dungeon Goblin|Win|2026-08-16|10|50\n"
        "4|5|Warrior Player|3|Dark Spider|Win|2026-08-16|20|100\n"
        "5|6|Rogue Player|2|Skeleton Warrior|Win|2026-08-16|15|75"
    )

    ensure_file_exists(files["enemy_difficulty"],
        "1|Easy|1.0|1.0\n"
        "2|Easy|1.0|1.0\n"
        "3|Medium|1.2|1.1\n"
        "4|Medium|1.2|1.1\n"
        "5|Hard|1.5|1.3\n"
        "6|Hard|1.5|1.3"
    )

    ensure_file_exists(files["starting_items"],
        "2|1|Health Potion|2\n"
        "3|1|Health Potion|3\n"
        "4|1|Health Potion|2\n"
        "5|1|Health Potion|1\n"
        "6|1|Health Potion|2"
    )

    ensure_file_exists(files["defeated_enemies"],
        "2|1\n"
        "3|2\n"
        "4|1\n"
        "5|3\n"
        "6|2"
    )

    ensure_file_exists(files["boss_status"],
        "2|No|N/A\n"
        "3|No|N/A\n"
        "4|No|N/A\n"
        "5|No|N/A\n"
        "6|No|N/A"
    )


# ========================= LOGIN MODULE =========================

def login_screen():
    """the purpose of this function is basically for logging in,
    this func checks if parts is greater than or equal to 4, then if so unpack the parts 
    into recognizable variable name.  if part is greater than 4, then get the 4th index
    if not, get the first index, but i mean it is second index, because of zero based indexing,
    now if acc user is equal to the player input and the pass, then login success, if not then its not,
    and if successful kogin, return a dict of them, if not then return None"""

    clear_screen()
    print_header("DUNGEON ESCAPE QUEST GAME")
    print("  Role-Based Login System")
    print("=" * 60)
    print()
    print("  GAME LOGIN")
    print("-" * 40)

    username = input("Username: ").strip()
    password = input("Password: ").strip()

    lines = read_file_lines(files["accounts"])
    for line in lines:
        parts = parse_record(line)
        if len(parts) >= 4:
            acc_id, acc_user, acc_pass, role, display_name = parts[0], parts[1], parts[2], parts[3], parts[4] if len(parts) > 4 else parts[1]
            if acc_user == username and acc_pass == password:
                print(f"\n  Login successful! Welcome, {display_name}!")
                pause()
                return {"id": acc_id, 
                        "username": acc_user, 
                        "role": role, 
                        "name": display_name}

    print("\n  Invalid username or password!")
    print("  Sample: admin/admin123 | player1/player123")
    pause()
    return None

# ========================= CRUD OPERATIONS =========================

def crud_menu(title, filename, fields_display, sample_data_func):
    """this one is for managing files, basically thats all there is to this"""
    while True:
        clear_screen()
        print_header(f"FILE MAINTENANCE - {title.upper()}")
        print("  [1] Add Record")
        print("  [2] View All Records")
        print("  [3] Search Record")
        print("  [4] Update Record")
        print("  [5] Delete Record")
        print("  [6] Back")
        print("=" * 60)

        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            add_record(filename, fields_display, sample_data_func) #if choice == 1 then call the add_record func, and put the parameters as its args
        elif choice == "2":
            view_all_records(filename, title)
        elif choice == "3":#Basically, all this r the same!
            search_record(filename, title)
        elif choice == "4":
            update_record(filename, fields_display)
        elif choice == "5":
            delete_record(filename, title)
        elif choice == "6":
            break
        else:
            print("  Invalid choice!")
            pause()

        
def add_record(filename, field_display, sample_data_func):
    """this is the add rec func, this gets called everytime the user input 1,
    so the job of this function is getting the existing id and generating,
    """

    clear_screen()
    print_header("ADD RECORD")

    existing_id = get_existing_ids(filename)
    new_id = generate_id(existing_id)
    print(f"  Generated ID: {new_id}")

    fields = [new_id]
    for field_name in field_display[1:]:
        value = input(f" Enter {field_name}: ").strip()
        if not value:
            print(f"  {field_name} cannot be empty!")
            pause()
            return
        fields.append(value)

    record_line = format_record(fields)
    append_to_file(filename, record_line)
    print(f"\n Record added successfully! ID: {new_id}")
    pause()

def view_all_records(filename, title):
    clear_screen()
    print_header(f"ALL {title.upper()} RECORDS")

    lines = read_file_lines(filename)
    if not lines:
        print("No records found")
    else:
        for i, line in enumerate(lines, 1):
            parts = parse_record(line)
            print(f" [{i}] {' | '.join(parts)}")

    print(f"\n Total Records: {len(lines)}")
    pause()

def search_record(filename, title):
    clear_screen()
    print_header(f"SEARCH {title.upper()}")

    search_id = input("Enter ID to search: ").strip()
    idx, record = find_record_by_id(filename, search_id)

    if record:
        print("\n Record Found:")
        print(f" {' | '.join(record)}")
    else:
        print("\n Record not found!")

    pause()

def update_record(filename, fields_display):
    clear_screen()
    print_header("UPDATE RECORD")

    update_id = input("  Enter ID to update: ").strip()
    idx, record = find_record_by_id(filename, update_id)

    if idx == -1:
        print("\n  Record not found!")
        pause()
        return
    
    print(f" Current Record: {' | '.join(record)}")
    print("  Enter new values (press Enter to keep current value):\n")

    new_record = [record[0]]
    for i, field_name in enumerate(fields_display[1:], 1):
        current = record[i] if i < len(record) else ""
        new_value = input(f" {field_name} [{current}]: ").strip()
        new_record.append(new_value if new_value else current)

    lines = read_file_lines(filename)
    lines[idx] = format_record(new_record)
    write_file_lines(filename, lines)
    
    print("\n  Record updated successfully!")
    pause()


def delete_record(filename, title):
    clear_screen()
    print_header("DELETE RECORD")

    delete_id = input("  Enter ID to delete: ").strip()
    idx, record = find_record_by_id(filename, delete_id)

    if idx == -1:
        print("\n Record not found!")
        pause()
        return

    print(f"\n  Record to delete: {' | '.join(record)}")
    confirm = input("  Are you sure? (y/n): ").strip().lower()

    if confirm == 'y':
        lines = read_file_lines(filename)
        lines.pop(idx)
        write_file_lines(filename, lines)
        print("\n  Record deleted successfully!")
    else:
        print("\n  Deletion cancelled.")
    
    pause()

# ========================= FILE MAINTENANCE MODULES =========================


def player_account_maintenance():
    crud_menu("Player Account Maintenance", files["accounts"], 
    ["ID", "Username", "Password", "Role", "Display Name"], None)

def enemy_maintenance():
    crud_menu("Enemy maintenance", files["enemies"],
     ["ID", "Name", "HP", "Attack", "Gold Reward", "Score Reward", "Is Boss", "Difficulty"], None)

def item_maintenance():
    crud_menu("Item Maintenance", files["items"], 
    ["ID", "Name", "Type", "Effect Value", "Description"], None)

def room_maintenance():
    crud_menu("Room Maintenance", files["rooms"], 
    ["ID", "Name", "Description", "Trap Damage", "Has Enemy", "Has Item"], None)

def question_maintenance():
    crud_menu("Question and Challenge Maintenance", files["questions"],
    ["ID", "Question", "Option A", "Option B", "Option C", "Option D", "Correct Answer"], None)


# ========================= GAME SETUP AND MANAGEMENT =========================

def game_setup_menu():
    while True:
        clear_screen()
        print_header("GAME SETUP AND MANAGEMENT")
        print("  [1] View Player Progress")
        print("  [2] Reset Player Game Data")
        print("  [3] Assign Starting Items")
        print("  [4] Set Enemy Difficulty")
        print("  [5] View Battle History")
        print("  [6] Back")
        print("=" * 60)

        choice = input(" Enter choice: ").strip()

        if choice == "1":
            view_player_prog()
        elif choice == "2":
            reset_data()
        elif choice == "3":
            assign_items()
        elif choice == "4":
            set_enemy_diff()
        elif choice == "5":
            view_batt_histo()
        elif choice == "6":
            break
        else:
            print("  Invalid choice!")
            pause()

        

def view_player_prog():
    clear_screen()
    print_header("VIEW PLAYER PROGRESS")

    lines = read_file_lines(files["player_progress"])
    if not lines:
        print(" No player progress found. ")
    else:
        print(f"""{'ID':<5}{'Name':<18}{'HP':<8}
        {'MaxHP':<8}{'Atk':<6}{'Pot':<6}{'Gold':<8}
        {'Score':<8}{'Room':<6}{'Boss':<6}""")

        print("-" * 80)
        for line in lines:
            parts = parse_record(line)
            if len(parts) >= 10:
                print(f"""{parts[0]:<5}{parts[1]:<18}{parts[2]:<8}{parts[3]:<8}
                {parts[4]:<6}{parts[5]:<6}{parts[6]:<8}{parts[7]:<8}{parts[8]:<6}
                {parts[9]:<6}""")

    pause()

def reset_data():
    clear_screen()
    print_header("RESET PLAYER GAME DATA")

    player_id = input("  Enter Player ID to reset: ").strip()
    idx, record = find_record_by_id(files["player_progress"], player_id)

    if idx == -1:
        print("\n  Player not found!")
        pause()
        return
    
    print(f"\n Player: {record[1]}")
    confirm = input(" Reset all game data? (y/n): ").strip().lower()

    if confirm == "y":
        lines = read_file_lines(files["player_progress"])
        name = record[1]
        new_record = [player_id, name, "100", "100", "10", "2", "0", "0", "1", "No"]
        lines[idx] = format_record(new_record)
        write_file_lines(files["player_progress"], lines)

        #defeated enimies that player has killed
        def_lines = read_file_lines(files["defeated_enemies"])
        def_lines = [l for l in def_lines if parse_record(l)[0] != player_id]
        write_file_lines(files["defeated_enemies"], def_lines)

        #reset boss
        boss_lines = read_file_lines(files["boss_status"])
        for i, line in enumerate(boss_lines):
            if parse_record(line)[0] == player_id:
                boss_lines[i] = f"{player_id}|No|N/A"
        write_file_lines(files["boss_status"], boss_lines)

        print("\n Player game data reset successfully!")

    else:
        print("\n  Reset cancelled.")

    pause()

def assign_items():
    clear_screen()
    print_header("ASSIGN STARTING ITEMS")

    player_id = input(" Enter Player ID: ").strip()
    idx, player = find_record_by_id(files["player_progress"], player_id)

    if idx == -1:
        print("\n  Player not found!")
        pause()
        return
    
    print(f"\n  Player: {player[1]}")
    print("\n  Available Items:")

    item_lines = read_file_lines(files["items"])
    for line in item_lines:
        parts = parse_record(line)
        print(f"  {parts[0]}. {parts[1]} ({parts[2]})")

    item_id = input("\n Enter item ID: ").strip()
    quantity = input(" Enter Quantity: ").strip()

    if not quantity.isdigit() or int(quantity) <= 0:
        print("\n Quantity must be a positive whole number!")
        pause()
        return

    item_idx, item = find_record_by_id(files["items"], item_id)
    if item_idx == -1:
        print("\n Item not found!")
        pause()
        return

    #update items that player starts with
    start_lines = read_file_lines(files["starting_items"])
    start_lines = [l for l in start_lines if not (parse_record(l)[0] == player_id and parse_record(l)[1] == item_id)]

    start_lines.append(f"{player_id}|{item_id}|{item[1]}|{quantity}")
    write_file_lines(files["starting_items"], start_lines)

    print(f"\n  Assigned {quantity}x {item[1]} to {player[1]}!")
    pause()

def set_enemy_diff():
    clear_screen()
    print_header("SET ENEMY DIFFICULTY")

    enemy_id = input(" Enter Enemy ID: ").strip()
    idx, enemy = find_record_by_id(files["enemies"], enemy_id)

    if idx == -1:
        print("\n  Enemy not found!")
        pause()
        return

    print(f"\n  Enemy: {enemy[1]}")
    print("  Difficulty Levels: Easy, Medium, Hard")

    diff = input("  Enter difficulty: ").strip()
    hp_mod = input(" Enter HP Modifier (e.g., 1.0, 1.5): ").strip()
    atk_mod = input("  Enter Attack Modifier (e.g., 1.0, 1.3): ").strip()

    if diff not in {"Easy", "Medium", "Hard"}:
        print("\n Invalid difficulty!")
        pause()
        return

    try:
        hp_modifier = float(hp_mod)
        atk_modifier = float(atk_mod)
    except ValueError:
        print("\n Modifiers must be numbers!")
        pause()
        return

    if hp_modifier <= 0 or atk_modifier <= 0:
        print("\n Modifiers must be greater than zero!")
        pause()
        return

    diff_lines = read_file_lines(files["enemy_difficulty"])
    diff_lines = [l for l in diff_lines if parse_record(l)[0] != enemy_id]
    diff_lines.append(f"{enemy_id}|{diff}|{hp_modifier}|{atk_modifier}")
    write_file_lines(files["enemy_difficulty"], diff_lines)

    print("\n  Enemy difficulty updated!")
    pause()


def view_batt_histo():
    clear_screen()
    print_header("BATTLE HISTORY")

    lines = read_file_lines(files["battle_history"])
    if not lines:
        print("  No battle history found.")
    else:
        print(f"""  {'ID':<5}{'Player':<18}{'Enemy':<20}{'Result':<8}
        {'Date':<12}{'Gold':<8}{'Score':<8}""")
        print("-" * 85)
        for line in lines:
            parts = parse_record(line)
            if len(parts) >= 9:
                print(f"""  {parts[0]:<5}{parts[2]:<18}{parts[4]:<20}{parts[5]:<8}
                {parts[6]:<12}{parts[7]:<8}{parts[8]:<8}""")

    pause()


def report_gen_menu():
    while True:
        clear_screen()
        print_header("REPORT GENERATION")
        print("  Select a report to view player and dungeon-game records.")

        print()
        print("  [1] Player Statistics Report")
        print("  [2] Battle Wins and Losses Report")
        print("  [3] Enemies Defeated Report")
        print("  [4] Player Score Ranking Report")
        print("  [5] Boss Defeat Status Report")
        print("  [6] Battle History Report")
        print("  [7] Available Items Report")
        print("  [8] Enemy Difficulty Report")
        print("  [9] Back")
        print("=" * 60)

        choice = input("  Enter choice: ").strip()

        reports = {
            "1": player_stats_rep,
            "2": battle_rep,
            "3": enemies_def_rep,
            "4": player_score_rep,
            "5": boss_def_stats_rep,
            "6": batt_histo,
            "7": available_items_rep,
            "8": enemy_difficulty_rep,
        }
        if choice in reports:
            reports[choice]()
        elif choice == "9":
            break
        else:
            print("  Invalid choice!")
            pause()


def player_stats_rep():
    clear_screen()
    print_header("PLAYER STATISTICS REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 70)

    lines = read_file_lines(files["player_progress"])
    if not lines:
        print("No data available")
    else:
        print(f""" {'Player':<20}{'HP':<10}{'Attack':<10}
        {'Potions':<10}{'Gold':<10}{'Score':<10}""")
        print("-" * 70)
        total_gold = 0
        total_score = 0
        for line in lines:
            parts = parse_record(line)
            if len(parts) >= 8:
                print(f"""  {parts[1]:<20}{parts[2]+'/'+parts[3]:<10}{parts[4]:<10}
                {parts[5]:<10}{parts[6]:<10}{parts[7]:<10}""")
                total_gold += int(parts[6])
                total_score += int(parts[7])
        print("-" * 70)
        print(f"""  {'TOTALS:':<20}{'':<10}
        {'':<10}{'':<10}{total_gold:<10}{total_score:<10}""")


def battle_rep():
    clear_screen()
    print_header("BATTLE WINS AND LOSSES REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 60)

    lines = read_file_lines(files["battle_history"])
    if not lines:
        print("  No data available.")
    else:
        wins = {}
        losses = {}
        for line in lines:
            parts = parse_record(line)
            if len(parts) < 6:
                continue
            player = parts[2]
            result = parts[5]
            if result == "Win":
                wins[player] = wins.get(player, 0) + 1
            else:
                losses[player] = losses.get(player, 0) + 1
        all_players = set(wins) | set(losses)
        print(f"  {'Player':<20}{'Wins':<10}{'Losses':<10}{'Win Rate':<10}")
        print("-" * 60)
        for player in sorted(all_players):
            w = wins.get(player, 0)
            l = losses.get(player, 0)
            total = w + l
            rate = f"{(w/total*100):.1f}%" if total > 0 else "0%"
            print(f"  {player:<20}{w:<10}{l:<10}{rate:<10}")

    pause()

def enemies_def_rep():
    clear_screen()
    print_header("ENEMIES DEFEATED REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 50)

    def_lines = read_file_lines(files["defeated_enemies"])
    enemy_lines = read_file_lines(files["enemies"])

    enemy_names = {}
    for line in enemy_lines:
        parts = parse_record(line)
        enemy_names[parts[0]] = parts[1]

    defeated_count = {}
    for line in def_lines:
        parts = parse_record(line)
        enemy_id = parts[1]
        defeated_count[enemy_id] = defeated_count.get(enemy_id, 0) + 1

    if not defeated_count:
        print("  No enemies defeated yet.")
    else:
        print(f"  {'Enemy':<25}{'Times Defeated':<15}")
        print("-" * 50)
        for enemy_id, count in sorted(defeated_count.items(), key=lambda x: x[1], reverse=True):
            name = enemy_names.get(enemy_id, "Unknown")
            print(f"  {name:<25}{count:<15}")

    pause()

def player_score_rep():
    clear_screen()
    print_header("PLAYER SCORE RANKING REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 50)

    lines = read_file_lines(files["player_progress"])
    if not lines:
        print("  No data available.")
    else:
        players = []
        for line in lines:
            parts = parse_record(line)
            players.append((parts[1], int(parts[7]), int(parts[6])))

        players.sort(key=lambda x: x[1], reverse=True)

        print(f"  {'Rank':<8}{'Player':<20}{'Score':<12}{'Gold':<10}")
        print("-" * 50)
        for i, (name, score, gold) in enumerate(players, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "  "
            print(f"  {medal}{i:<6}{name:<20}{score:<12}{gold:<10}")

    pause()

def boss_def_stats_rep():
    clear_screen()
    print_header("BOSS DEFEAT STATUS REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 60)

    lines = read_file_lines(files["boss_status"])
    if not lines:
        print("  No data available.")
    else:
        print(f"  {'Player':<20}{'Boss Defeated':<15}{'Date Defeated':<15}")
        print("-" * 60)
        defeated = 0
        for line in lines:
            parts = parse_record(line)
            status = "✓ YES" if parts[1] == "Yes" else "✗ No"
            if parts[1] == "Yes":
                defeated += 1
            print(f"  {parts[0]:<20}{status:<15}{parts[2]:<15}")
        print("-" * 60)
        print(f"  Total Players: {len(lines)}  |  Boss Defeated: {defeated}")

    pause()

def batt_histo():
    clear_screen()
    print_header("BATTLE HISTORY REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 90)

    lines = read_file_lines(files["battle_history"])
    if not lines:
        print("  No battle history found.")
    else:
        print(f"  {'ID':<5}{'Player':<18}{'Enemy':<20}{'Result':<8}{'Date':<12}{'Gold':<8}{'Score':<8}")
        print("-" * 90)
        total_gold = 0
        total_score = 0
        for line in lines:
            parts = parse_record(line)
            if len(parts) >= 9:
                print(f"  {parts[0]:<5}{parts[2]:<18}{parts[4]:<20}{parts[5]:<8}{parts[6]:<12}{parts[7]:<8}{parts[8]:<8}")
                total_gold += int(parts[7])
                total_score += int(parts[8])
        print("-" * 90)
        print(f"  {'TOTALS:':<5}{'':<18}{'':<20}{'':<8}{'':<12}{total_gold:<8}{total_score:<8}")

    pause()

def available_items_rep():
    clear_screen()
    print_header("AVAILABLE ITEMS REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 70)

    lines = read_file_lines(files["items"])
    if not lines:
        print("  No items available.")
    else:
        print(f"  {'ID':<5}{'Name':<20}{'Type':<12}{'Effect':<10}{'Description':<25}")
        print("-" * 70)
        for line in lines:
            parts = parse_record(line)
            print(f"  {parts[0]:<5}{parts[1]:<20}{parts[2]:<12}{parts[3]:<10}{parts[4]:<25}")

    pause()

def enemy_difficulty_rep():
    clear_screen()
    print_header("ENEMY DIFFICULTY REPORT")
    print(f"  Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("-" * 70)

    enemy_lines = read_file_lines(files["enemies"])
    diff_lines = read_file_lines(files["enemy_difficulty"])

    diff_map = {}
    for line in diff_lines:
        parts = parse_record(line)
        diff_map[parts[0]] = parts[1:]

    if not enemy_lines:
        print("  No enemy data available.")
    else:
        print(f"  {'Enemy':<20}{'Base HP':<10}{'Base Atk':<10}{'Difficulty':<12}{'HP Mod':<10}{'Atk Mod':<10}")
        print("-" * 70)
        for line in enemy_lines:
            parts = parse_record(line)
            diff = diff_map.get(parts[0], ["Default", "1.0", "1.0"])
            print(f"  {parts[1]:<20}{parts[2]:<10}{parts[3]:<10}{diff[0]:<12}{diff[1]:<10}{diff[2]:<10}")

    pause()

# ========================= ADMIN MODULE =========================

def admin_menu(user):
    while True:
        clear_screen()
        print_header("DUNGEON ESCAPE QUEST GAME")
        print(f"  Logged in as: {user['name']} | Role: {user['role']}")
        print("=" * 60)
        print("  ADMIN MENU")
        print("-" * 60)
        print("  [1] File Maintenance")
        print("  [2] Game Setup and Management")
        print("  [3] Report Generation")
        print("  [4] Logout")
        print("=" * 60)

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            file_maintenance_menu()
        elif choice == "2":
            game_setup_menu()
        elif choice == "3":
            report_gen_menu()
        elif choice == "4":
            print("\n  Logging out...")
            pause()
            break
        else:
            print("  Invalid choice!")
            pause()

def file_maintenance_menu():
    while True:
        clear_screen()
        print_header("FILE MAINTENANCE")
        print("  [1] Player Account Maintenance")
        print("  [2] Enemy Maintenance")
        print("  [3] Item Maintenance")
        print("  [4] Room Maintenance")
        print("  [5] Question and Challenge Maintenance")
        print("  [6] Back")
        print("=" * 60)

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            player_account_maintenance()
        elif choice == "2":
            enemy_maintenance()
        elif choice == "3":
            item_maintenance()
        elif choice == "4":
            room_maintenance()
        elif choice == "5":
            question_maintenance()
        elif choice == "6":
            break
        else:
            print("  Invalid choice!")
            pause()

# ========================= BATTLE GAME MODULE =========================

def get_player_progress(player_id):
    idx, record = find_record_by_id(files["player_progress"], player_id)
    if idx == -1:
        return None
    return {
        "id": record[0],
        "name": record[1],
        "hp": int(record[2]),
        "max_hp": int(record[3]),
        "attack": int(record[4]),
        "potions": int(record[5]),
        "gold": int(record[6]),
        "score": int(record[7]),
        "room": int(record[8]),
        "boss_defeated": record[9]
    }

def save_player_progress(progress):
    lines = read_file_lines(files["player_progress"])
    for i, line in enumerate(lines):
        if line.startswith(progress["id"] + "|"):
            lines[i] = format_record([
                progress["id"], progress["name"], str(progress["hp"]),
                str(progress["max_hp"]), str(progress["attack"]),
                str(progress["potions"]), str(progress["gold"]),
                str(progress["score"]), str(progress["room"]),
                progress["boss_defeated"]
            ])
            break
    write_file_lines(files["player_progress"], lines)

def get_enemy_for_room(room_id):
    try:
        room_id = int(room_id)
    except (TypeError, ValueError):
        return None

    room_idx, room = find_record_by_id(files["rooms"], str(room_id))
    if room_idx == -1 or len(room) < 5 or room[4] != "Yes":
        return None

    enemy_lines = read_file_lines(files["enemies"])
    if not enemy_lines:
        return None

    enemy_index = (room_id - 1) % len(enemy_lines)
    enemy_data = parse_record(enemy_lines[enemy_index])
    if len(enemy_data) < 7:
        return None

    diff_idx, diff = find_record_by_id(files["enemy_difficulty"], enemy_data[0])
    hp_mod = 1.0
    atk_mod = 1.0
    if diff_idx != -1 and len(diff) >= 4:
        try:
            hp_mod = float(diff[2])
            atk_mod = float(diff[3])
        except ValueError:
            pass

    try:
        base_hp = int(enemy_data[2])
        base_attack = int(enemy_data[3])
        gold_reward = int(enemy_data[4])
        score_reward = int(enemy_data[5])
    except ValueError:
        return None

    return {
        "id": enemy_data[0],
        "name": enemy_data[1],
        "hp": int(base_hp * hp_mod),
        "max_hp": int(base_hp * hp_mod),
        "attack": int(base_attack * atk_mod),
        "gold_reward": gold_reward,
        "score_reward": score_reward,
        "is_boss": enemy_data[6] == "Yes"
    }

def is_enemy_defeated(player_id, enemy_id):
    lines = read_file_lines(files["defeated_enemies"])
    for line in lines:
        parts = parse_record(line)
        if parts[0] == player_id and parts[1] == enemy_id:
            return True
    return False

def mark_enemy_defeated(player_id, enemy_id):
    append_to_file(files["defeated_enemies"], f"{player_id}|{enemy_id}")

def record_battle_history(player_id, player_name, enemy_id, enemy_name, result, gold, score):
    existing_ids = get_existing_ids(files["battle_history"])
    new_id = generate_id(existing_ids)
    date_str = datetime.now().strftime("%Y-%m-%d")
    line = format_record([new_id, player_id, player_name, enemy_id, enemy_name, result, date_str, str(gold), str(score)])
    append_to_file(files["battle_history"], line)

def get_random_question():
    lines = read_file_lines(files["questions"])
    if not lines:
        return None
    return parse_record(random.choice(lines))

def battle_game(player):
    player_id = player["id"]
    progress = get_player_progress(player_id)

    if not progress:
        print("\n  Error: Player progress not found! Contact Admin.")
        pause()
        return

    if progress["boss_defeated"] == "Yes":
        print("\n  You have already escaped the dungeon! You are free!")
        pause()
        return

    current_room = progress["room"]
    enemy = get_enemy_for_room(current_room)

    while progress["hp"] > 0:
        clear_screen()
        print_header("DUNGEON ESCAPE BATTLE GAME")
        print(f"  Choose an action for your current dungeon encounter.")
        print()
        print(f"  HP: {progress['hp']}/{progress['max_hp']}   Attack: {progress['attack']}   Potions: {progress['potions']}   Gold: {progress['gold']}   Score: {progress['score']}")

        if not enemy:
            print("\n  This room is empty. Moving to next room...")
            current_room = (current_room % 6) + 1
            progress["room"] = current_room
            save_player_progress(progress)
            pause()
            enemy = get_enemy_for_room(current_room)  
            continue

       
        if is_enemy_defeated(player_id, enemy["id"]):
            print(f"\n  You have already defeated the {enemy['name']} in this room!")
            print("  Moving to next room...")
            current_room = (current_room % 6) + 1
            progress["room"] = current_room
            save_player_progress(progress)
            pause()
            enemy = get_enemy_for_room(current_room)  
            continue

        print(f"\n  Current Encounter: {enemy['name']} | Enemy HP: {enemy['hp']}/{enemy['max_hp']}")
        if enemy["is_boss"]:
            print("  ⚠️  WARNING: This is the FINAL BOSS!")
        print()
        print("  [1] Attack")
        print("  [2] Defend")
        print("  [3] Use Item")
        print("  [4] Answer Challenge Question")
        print("  [5] Attempt Escape")
        print("=" * 60)

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            damage = progress["attack"]
            enemy["hp"] -= damage
            print(f"\n  You attacked {enemy['name']} for {damage} damage!")

            if enemy["hp"] <= 0:
                print(f"\n  🎉 You defeated {enemy['name']}!")
                progress["gold"] += enemy["gold_reward"]
                progress["score"] += enemy["score_reward"]
                mark_enemy_defeated(player_id, enemy["id"])
                record_battle_history(player_id, progress["name"], enemy["id"], enemy["name"], "Win", enemy["gold_reward"], enemy["score_reward"])

                if enemy["is_boss"]:
                    progress["boss_defeated"] = "Yes"
                    print("\n  🏆 CONGRATULATIONS! You defeated the Final Boss!")
                    print("  You have escaped the dungeon and WON THE GAME!")
                    boss_lines = read_file_lines(files["boss_status"])
                    for i, line in enumerate(boss_lines):
                        if line.startswith(player_id + "|"):
                            boss_lines[i] = f"{player_id}|Yes|{datetime.now().strftime('%Y-%m-%d')}"
                    write_file_lines(files["boss_status"], boss_lines)

                save_player_progress(progress)
                pause()

                if enemy["is_boss"]:
                    return

    
                current_room = (current_room % 6) + 1
                progress["room"] = current_room
                save_player_progress(progress)
                enemy = get_enemy_for_room(current_room)
            else:
               
                enemy_damage = max(0, enemy["attack"] - random.randint(0, 3))
                progress["hp"] -= enemy_damage
                print(f"  {enemy['name']} counter-attacked for {enemy_damage} damage!")
                print(f"  Your HP: {max(0, progress['hp'])}/{progress['max_hp']}")
                print(f"  Enemy HP: {enemy['hp']}/{enemy['max_hp']}")
                save_player_progress(progress)
                pause()

        elif choice == "2":
        
            print(f"\n  You raised your guard!")
            enemy_damage = max(0, enemy["attack"] // 2 - random.randint(0, 2))
            progress["hp"] -= enemy_damage
            print(f"  {enemy['name']} attacked but you blocked most of it!")
            print(f"  You took only {enemy_damage} damage!")
            print(f"  Your HP: {max(0, progress['hp'])}/{progress['max_hp']}")
            save_player_progress(progress)
            pause()

        elif choice == "3":
       
            if progress["potions"] > 0:
                heal_amount = 30
                progress["potions"] -= 1
                progress["hp"] = min(progress["max_hp"], progress["hp"] + heal_amount)
                print(f"\n  You used a Health Potion!")
                print(f"  Restored {heal_amount} HP!")
                print(f"  Your HP: {progress['hp']}/{progress['max_hp']}")
                print(f"  Potions remaining: {progress['potions']}")
                save_player_progress(progress)
            else:
                print("\n  You have no potions!")
            pause()

        elif choice == "4":
          
            question = get_random_question()
            if question:
                print(f"\n  CHALLENGE QUESTION:")
                print(f"  {question[1]}")
                print(f"  A) {question[2]}")
                print(f"  B) {question[3]}")
                print(f"  C) {question[4]}")
                print(f"  D) {question[5]}")

                answer = input("\n  Your answer (A/B/C/D): ").strip().upper()

                if answer == question[6]:
                    bonus_damage = progress["attack"] * 2
                    enemy["hp"] -= bonus_damage
                    print(f"\n  ✓ Correct! You dealt {bonus_damage} bonus damage!")

                    if enemy["hp"] <= 0:
                        print(f"\n  🎉 You defeated {enemy['name']} with your knowledge!")
                        progress["gold"] += enemy["gold_reward"]
                        progress["score"] += enemy["score_reward"]
                        mark_enemy_defeated(player_id, enemy["id"])
                        record_battle_history(player_id, progress["name"], enemy["id"], enemy["name"], "Win", enemy["gold_reward"], enemy["score_reward"])

                        if enemy["is_boss"]:
                            progress["boss_defeated"] = "Yes"
                            print("\n  🏆 CONGRATULATIONS! You defeated the Final Boss!")
                            print("  You have escaped the dungeon and WON THE GAME!")
                            boss_lines = read_file_lines(files["boss_status"])
                            for i, line in enumerate(boss_lines):
                                if line.startswith(player_id + "|"):
                                    boss_lines[i] = f"{player_id}|Yes|{datetime.now().strftime('%Y-%m-%d')}"
                            write_file_lines(files["boss_status"], boss_lines)

                        save_player_progress(progress)
                        pause()

                        if enemy["is_boss"]:
                            return

                        
                        current_room = (current_room % 6) + 1
                        progress["room"] = current_room
                        save_player_progress(progress)
                        enemy = get_enemy_for_room(current_room)
                    else:
                        print(f"  Enemy HP: {enemy['hp']}/{enemy['max_hp']}")
                        pause()
                else:
                    print(f"\n  ✗ Wrong! The correct answer was {question[6]}.")
                    enemy_damage = enemy["attack"]
                    progress["hp"] -= enemy_damage
                    print(f"  {enemy['name']} attacked for {enemy_damage} damage!")
                    print(f"  Your HP: {max(0, progress['hp'])}/{progress['max_hp']}")
                    save_player_progress(progress)
                    pause()
            else:
                print("\n  No questions available!")
                pause()

        elif choice == "5":
          
            if enemy["is_boss"] and progress["boss_defeated"] != "Yes":
                print("\n  ⚠️  You cannot escape without defeating the Final Boss!")
                pause()
            else:
                escape_chance = random.random()
                if escape_chance > 0.5:
                    print("\n  You successfully escaped from the encounter!")
                    current_room = (current_room % 6) + 1
                    progress["room"] = current_room
                    save_player_progress(progress)
                    enemy = get_enemy_for_room(current_room)  
                else:
                    print("\n  Escape failed!")
                    enemy_damage = enemy["attack"] + 5
                    progress["hp"] -= enemy_damage
                    print(f"  {enemy['name']} hit you for {enemy_damage} damage as you tried to flee!")
                    print(f"  Your HP: {max(0, progress['hp'])}/{progress['max_hp']}")
                    save_player_progress(progress)
                pause()

        else:
            print("\n  Invalid choice!")
            pause()

     
        if progress["hp"] <= 0:
            progress["hp"] = 0
            save_player_progress(progress)
            clear_screen()
            print_header("GAME OVER")
            print(f"\n  💀 You have been defeated by {enemy['name']}!")
            print(f"\n  Final Statistics:")
            print(f"  Score: {progress['score']}")
            print(f"  Gold: {progress['gold']}")
            print(f"  Rooms Cleared: {current_room - 1}")
            record_battle_history(player_id, progress["name"], enemy["id"], enemy["name"], "Loss", 0, 0)
            print("\n  Your progress has been saved. Try again!")
            pause()
            return

# ========================= PLAYER MODULE =========================

def player_menu(user):
    while True:
        clear_screen()
        print_header("DUNGEON ESCAPE QUEST GAME")
        print(f"  Logged in as: {user['name']} | Role: {user['role']}")
        print("=" * 60)
        print("  PLAYER MENU")
        print("-" * 60)
        print("  Welcome, Player!")
        print("  You can only access the Battle Game.")
        print("  Select Start Battle Game to begin your dungeon quest.")
        print()
        print("  [1] Start Battle Game")
        print("  [2] Logout")
        print("=" * 60)

        choice = input("  Enter choice: ").strip()

        if choice == "1":
            battle_game(user)
        elif choice == "2":
            print("\n  Logging out...")
            pause()
            break
        else:
            print("  Invalid choice!")
            pause()

# ========================= MAIN PROGRAM =========================

def main():
    initialize_system()

    while True:
        user = login_screen()
        if user:
            if user["role"] == "Admin":
                admin_menu(user)
            elif user["role"] == "Player":
                player_menu(user)
            else:
                print("  Unknown role!")
                pause()

if __name__ == "__main__":
    main()

