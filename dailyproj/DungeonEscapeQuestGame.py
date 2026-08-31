import os
import random
from datetime import datetime

#===========================FILENAMES========================================
files = {
    "accounts": "account.txt",
    "enemies": "enemies.txt",
    "rooms": "rooms.txt",
    "questions": "questions.txt",
    "player_progress": "player_progress.txt",
    "battle_history": "battle_history.txt",
    "enemy_difficulty": "enemy_difficulty.txt",
    "starting_enemies": "starting_enemies.txt",
    "defeated_enemies": "defeated_enemies.txt",
    "boss_status": "boss_status.txt",

}

#=======================UTILITY FUNCTIONS====================================

def ensure_file_exists(filename, default_content=""):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(default_content)

            
def read_file_lines(filename):
    ensure_file_exists(filename)
    with open(filename, "r") as f:
        return[line.strip() for line in f if line.strip()]


def write_file_lines(filename, lines):
    with open(filename, "w") as f:
        for line in lines:
            f.write(line + "\n")

def append_to_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

def parse_record(line, delimiter="|"):
    return [field.strip() for field in line.split(delimiter)]

def format_record(fields, delimiter="|"):
    return delimiter.join(str(f) for f in fields)

def generate_id(existing_ids):
    if not existing_ids:
        return "1"
    max_id = max(int(i) for i in existing_ids if i.isdigit())
    return str(max_id + 1)

def get_existing_ids(filename):
    lines = read_file_lines(filename)
    ids = []
    for line in lines:
        parts = parse_record(line)
        if parts:
            ids.append(parts[0])
        
    return ids

def find_record_by_id(filename, record_id):
    lines = read_file_lines(filename)
    for i, line in enumerate(lines):
        parts = parse_record(line)
        if parts and parts[0] == str(record_id):
            return i, parts 
    return -1, None 

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    print('=' * 60)
    print(f'  {title:^56}')
    print('=' * 60)

def pause():
    input("Press Enter to continue...")

#=============================INITILLIZATION===========================

def initialize_system():
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

    ensure_file_exists(FILES["boss_status"],
        "2|No|N/A\n"
        "3|No|N/A\n"
        "4|No|N/A\n"
        "5|No|N/A\n"
        "6|No|N/A"
    )


# ========================= LOGIN MODULE =========================

def login_screen():
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


















def add_record(fiilename, field_display, sample_data_func):
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
        new_value = input(f" {fieldn_name} [{current}]: ").strip()
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
        line.pop(idx)
        write_file_lines(filename, lines)
        print("\n  Record deleted successfully!")
    else:
        print("\n  Deletion cancelled.")
    
    pause()












            








 