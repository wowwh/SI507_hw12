import json
from datetime import datetime

GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id=0

def init():
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    time_string = str(now)

    # if you have an error using this format, just use
    # time_string = str(now)
    if len(entries)>0:
        next_id=entries[0]['id']+1
    entry = {"author": name, "text": text, "timestamp": time_string,"id":next_id}
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for e in entries:
        if str(e['id']) == str(id):
            # entry = {"author": 'haha', "text": 'haha', "timestamp": 'haha',"id":7777}            
            # entries.insert(0, entry)
            # entries.pop(entries.index(e))
            entries.remove(e)
            break
            

    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")