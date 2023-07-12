print("################### LIST TASKS ########################")
# from pynative.com

print("-----------TASK 1----------------------")
print("")
print("")

list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)





print("-----------TASK 2----------------------------------*****------")
print("")
print("")

# Program to add 2 lists index wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "ly"]

# für jedes i, j  der beiden, sich in der zip befindenden lists, füge i+j in eine neue liste hinzu
list_result = [i + j for i, j in zip(list1, list2)]    
print((list_result))





print("-----------TASK 3: all elements to square----------------------")
print("")
print("")

numbers = [1,2,3,4,5,6,7]

list2 = [num ** 2 for num in numbers]
print(list2)





print("-----------TASK 4: Concatinating 2 lists-------------------*****------")
print("")
print("")

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# du kannst 2 for loops hintereinander machen bei comprehensive
result = [i + j for i in list1 for j in list2]
print(result)





print("-----------TASK 5: 2 gleichzeitig iterieren--------------------*****--")
print("")
print("")

list1 = [10,20,30,40]
list2 = [100, 200, 300, 400]

# mit zip immer die ersten paare abgereifen und dann die liste2 aber von hinten aufzäumen mit ::-1
for i, j in zip(list1, list2[::-1]):
    print(i, j)





print("-----------TASK 6: remove empty strings from lst of str-----------")
print("")
print("")

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

result = []
for name in list1:
    if name != "":
        result.append(name)
print(result)



# kürzere alternative:

res = list(filter(None, list1))
print(res)





print("-----------TASK 7: neues item hinter spezifischem item in liste hinzufügen----------------------")
print("")
print("")

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)





print("-----------TASK 8: erweitere nestesd liste um eine subliste-------------------*---")
print("")
print("")

list1 = ["a", "b", ["c",["d", "e",["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)





print("-----------TASK 9: replace das erste spez. item 20 mit einem anderen wert 200---------------*****---")
print("")
print("")

list1 = [5, 10, 15, 20, 25, 50, 20]

#keine ahunng , warum nur die erste 20 ersetzt wird
index = list1.index(20)
list1[index] = 200

print(list1)





print("-----------TASK 10: remove alle spezifischen items (hier 20) aus einer liste------------------")
print("")
print("")

list1 = [5, 20, 15, 20, 25, 50, 20]

for num in list1:
    if num == 20:
        list1.remove(num)
print(list1)
    




print("################### TUPLE TASKS ########################")
# from pynative.com

print("-----------TASK 1: reverse tuple------------------")
print("")
print("")

# man sliced eben
tuple1 = (10, 20, 390, 40, 50)

print(tuple1[::-1])




print("-----------TASK 2: nested tuple, programm schreiben, ads die value 20 ausgibt------------------")
print("")
print("")

tuple1 = ("Orange", [10, 20, 30], (5,15,25))
print(tuple1[1][1])




print("-----------TASK 3: create tuple mit edm einzigen item 50-------------* (erst nur 50 eingegeben)-----")
print("")
print("")

tuple1 = (50, )
print(tuple1)




print("-----------TASK 4: tuple entpacken in jeweils eine var pro item----------------------*****--")
print("")
print("")

tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
print(a, b, c, d)




print("-----------TASK 5: tausche zwei tuples-------------*-----------")
print("")
print("")

tuple1 = (11, 22)
tuple2 = (99, 88)


tuple1, tuple2 = tuple2, tuple1 
print(tuple1)
print(tuple2)





print("-----------TASK 6: bestimmte items eines tuples in einen euen tuple einfugen-------------***-----------")
print("")
print("")

tuple1 = (11,22,33,44,55,66)

if 44 and 55 in tuple1:
    tuple2 = (44,55)
print(tuple2)


# nach betrachten der lösung.. einfach 44 und 55 eines tuples in neuen tuple
tuple2 = tuple1[3:5]   #alternative
print(tuple2)
tuple2 = tuple1[3:-1]  
print(tuple2)





print("-----------TASK 7: Tuples modify------------------------")
print("")
print("")

tuple1 = (11, [22,33], 44,55)

tuple1[1][0] = 222
print(tuple1)




print("-----------TASK 8: tuple von tuples nach ihrem 2. item sortieren-----------*****-------------")
print("")
print("")

# du sortierst die items des zur liste gemachten tuple1 nach dem 2. item und gibst das wieder als tuple aus. 
# hierfür kannst du bei der method sorted(), bei der die zu ordnende liste als 1. arg steht für den key eine lambda funktoin nutzen
# die von den listen-items jeweils den wert de 2. indecees nimm,t (lamda x: x[1]) 
tuple1 = (("a", 23), ("b", 37), ("c", 11), ("d", 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)




print("-----------TASK 9: häufigkeit eines bestimmten items in einem tuple ausgeben------------------------")
print("")
print("")

tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))




print("-----------TASK 10: check ob alle items in dem tuple identisch sind------------------------")
print("")
print("")

tuple1 = (45,45,45,45)

i = tuple1[0]
for num in tuple1:
    if num == i:
        x = True
    else:
        x = False
print(x)


