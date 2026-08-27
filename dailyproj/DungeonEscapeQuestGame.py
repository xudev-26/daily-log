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
    with open(filename, "a") as f:
        f.write(line + "\n")

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
    

        