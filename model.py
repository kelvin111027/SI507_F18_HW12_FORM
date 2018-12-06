
import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
id = 0


def init():
    global entries
    global id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        id_max = 0
        for p in entries:
            if id_max < int(p['id']):
                id_max = int(p['id'])
        id = id_max
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE
    global id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %I:%M %p")
    # if you have an error using this format, just use
    # time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": str(id+1)}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete(id_del):
    global entries, GUESTBOOK_ENTRIES_FILE
    entries_new = []
    for p in entries:
        if p["id"] !=  id_del:
            entries_new.insert(0, p)
    entries = entries_new
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")
