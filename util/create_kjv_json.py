#!/usr/bin/env python3
import os
import json
from typing import Dict

def handletwoPartBookName(line: str, count: int) -> Dict:
    broken = line.split()
    book = ''.join(broken[0:2])
    chapter, verse = broken[2].split(":")
    text = text = " ".join(broken[3:])
    return {"book": book,
            "chapter": chapter,
            "verse": verse,
            "text": text,
            "ordinal_verse": count}

def handleSongOfSolomon(line: str, count: int) -> Dict:
    broken = line.split()
    book = ''.join(broken[0:3])
    chapter, verse = broken[3].split(":")
    text = text = " ".join(broken[4:])
    return {"book": book,
            "chapter": chapter,
            "verse": verse,
            "text": text,
            "ordinal_verse": count}

def readBible():
    bible_json = []
    bible_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../data/bible.txt")
    print("bible_path: {}".format(bible_path))
    bible_file = open(bible_path, 'r')
    count = 0

    while count <= 31102:
        print("starting over..: ", count)
        count += 1
        line = bible_file.readline()
        broken = line.split()
        if line == "":
            break
        # 1 Samuel - 2 Chronicals
        if count >= 7214 and count <= 12017:
            bible_json.append(handletwoPartBookName(line, count))
            continue
        # Song of Solomon
        elif count >= 17539 and count <= 17655:
            bible_json.append(handleSongOfSolomon(line, count))
            continue
        # 1 Corinthians - 2 Corinthians
        elif count >= 28365 and count <= 29058:
            bible_json.append(handletwoPartBookName(line, count))
            continue
        # 1 Thessalonians - 2 Timothy
        elif count >= 29562 and count <= 29893:
            print(line)
            print(count)
            bible_json.append(handletwoPartBookName(line, count))
            continue
        # 1 Peter - 3 John
        elif count >= 30376 and count <= 30673:
            bible_json.append(handletwoPartBookName(line, count))
            continue
        else:
            chapter, versenum = broken[1].split(":")
            book = broken[0]
            ordinal_versenum = count
            bible_text = " ".join(broken[2:])
            bible_json.append({"book": book,
                               "chapter": chapter,
                               "verse": versenum,
                               "text": bible_text,
                               "ordinal_verse": ordinal_versenum})
        if count > 31102:
            break
        
        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))
    bible_file.close()
    
    print(json.dumps(bible_json, indent=4))
    json_bible_path = "/tmp/kjv.json"
    with open(json_bible_path, 'w') as jb:
        jb.write(json.dumps(bible_json, indent=4))
        
if __name__ == '__main__':
    print("Starting.")
    readBible()
