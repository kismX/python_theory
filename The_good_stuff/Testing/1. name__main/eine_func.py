###################"Verstehen des __name__ == __main__ "##############################

# ich erstelle irgendeine funktion, die ich testen will
def task(a,b):
    res = a*b
    return res


# ich schreibe eine willkürlichen test: wenn das ergebnis von task positiv ist, dann soll alles ok sein:
# diese wurde auskommentiert, weil ich weiter unten etwas ergänzt habe

# if task(1,3) > 1:
#     print("all ok")
# else:
#     print("not ok")


# wenn ich die nächsten zeilen nciht schreiben würde, würde jedes mal, wenn ich dieses modul (eine_func.py) 
# irgendwo importiere, das printstatement der testzeilen ausgegeben werden.
# das liegt daran, dass das attribut __main__ eines moduls, das mit bsow eine_func.py abgespeichert wird
# beim importieren den wert "eine_func" annimmt. wird die datei eine_func.py als programm aufgerufen nimmt __name__ dann den wert __main an.

if __name__ == "__main__":
    if task(1,3) > 1:
        print("all ok")
    else:
        print("not ok")

