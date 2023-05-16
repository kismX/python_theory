## Exercise (Vowel Sort):
#Write a Python program that sorts a list of strings based on the number of vowels they contain.
#The program should take a list of strings as input from the user.
#sort the strings by the number of vowels they contain using the sort() method with a custom function
#print the sorted list of strings.

print('------------TRIALS to SOLVE------------')
print()
print()


vowels = "AEIOUaeiou"
user_input = input("Enter some words: ")
word_list = user_input.split(",")  #lsis mit eingegebenen wörtern
counted_list = []

for word in word_list:
    count = 0
    for letter in range(len(word)):
        if word[letter] in vowels:
            count += 1
    counted_list.append((word, count))

def new_list(item_in_counted_list):
    return item_in_counted_list[1]

print(sorted(counted_list, key=new_list))


print('-------------TASK2-------------')


## Exercise (sort by second element):
# Write a Python program that sorts a list of tuples based on the second element of each tuple.
# The program should take a list of tuples as input from the user,
# sort the tuples by the second element using the sort() method with a custom function
# print the sorted list of tuples

tuple_list = [(2, 5), (1, 7), (4, 3), (6, 1), (3, 8)] #-->   [(6, 1), (4, 3), (2, 5), (1, 7), (3, 8)]

print()
print()
print("-------------------------------------------------")
print('---------------------DUCS Lösung-Task------------')
print("-------------------------------------------------")
print()
print()


# # Write a Python program that sorts a list of strings based on the number
#  of vowels they contain.
# # The program should take a list of strings as input from the user.
# # sort the strings by the number of vowels they contain using the sort() 
# # method with a custom function
# # print the sorted list of strings.

#COUNT VOWELS
def vowel_counter(word):
    counter=0
    vowels="AEIOUaeiou"  #List of all Voals​

    for i in range(0,len(word)):  #Loop through every character in word
        if word[i] in vowels: #wenn Character in der Liste
            counter+=1

    return counter
    
#Function to create List
def get_list():
    lst=[]
    number=int(input("How Many Words do you want in the list?"))

    for i in range(number):
        word=input(f"Enter Word {i+1}: ")
        lst.append(word)
    return lst

list_string=get_list()
print("Before Sorting: ")
print(list_string)

print("\nAfter Sorting:")
sorted_list_string=sorted(list_string,key=vowel_counter)
print(sorted_list_string)



    
    # counted = [word.count(vowels) for word in my_strings]




#my_strings = [input("Giv us a few words: ")]
#print(vowel_check(my_strings))



print()
print()
print("------------------TASK 2-------------------------------")
print()
print()

# Write a Python program that sorts a list of tuples based on the second element of each tuple.
# The program should take a list of tuples as input from the user,
# sort the tuples by the second element using the sort() method with a custom function
# print the sorted list of tuples