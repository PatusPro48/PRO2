import os
with open(os.sep.join(["slozka", "testhod2.txt"]), encoding="utf-8") as soubor:
    text = soubor.read()
    print(text)
