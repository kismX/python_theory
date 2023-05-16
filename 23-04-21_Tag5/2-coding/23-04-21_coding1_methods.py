# String Methods
# es gibt sehr viele, du kannst sie ergooglen docs.python.org zb

my_text = "this is a TEST"
print(my_text.upper())          # .UPPER macht alles zu großbuchstaben
print(my_text.capitalize())     # macht ersten Buchstaben Groß, rest klein
print(my_text.lower())          # kleinbuchgstaben
print(my_text.isalpha())        # schaut ob string ist nur alphabetisch, dann True, wenn leerzeichen dann False
print(my_text.isalnum())        # schaut ob nur nummern enthalten allnum = alphanumeric
print(my_text.split())          # split the string from spaces into a list
print(my_text.split("a"))       # splittet the string from "a" character


long_text = '''It was a dark an stormy night
ya ya , ding dong and stuff
The End.'''
print(long_text.split("\n"))    # zb splkitten bei zeilenum,bruch mit \n und du hast jede zeile als item in einer list


print("A nice kitten".replace("kitten", "dragon"))   # man kann diese methods auch direkt im print nutzen .. # hier mit replace-method als bsp

desc = "A mage conjured an image of a dragon"
print(desc.replace("mage", "wizard"))               # hier ist auch das "mage" vom image gewechselt worden



# What is the "\" charactoer called again?
# is is the escape character in python
# there are a few such escape characters in py. you should google for more
text = "rauli\n\tStr: 3\n\tInt: 2\n\tHP: 7"    #\n ist zeilenumbruch \t setzt ein tab
text2 = "joel \"Req\" Peltonen"
print(text)

print("-----------------------")

print(len("caramel ice"))               # len() gibt number of items in a container, hier 11 zeichen im string
print(len(["Water", "Snow", "Ice"]))    # hier 3 items im container , hier liste mit 3 items
# print(len(124235345))                   # len() kann kein integer --> error

print("-------------------------")
###################methods with lists
drinks = ["Coffee", "Tea", "Water"]  # mache eine liste mit namen "drinks"
print(drinks[0])   # printed 1 item der list aus
print(drinks[0][2])  # printet von item1 den dritten buchstaben aus

drinks.append("Juice")  # fügt ein item der liste hinzu
drinks.append(7)        # man kann auch andere datatypes hinzufügen in die liste
print(drinks)





