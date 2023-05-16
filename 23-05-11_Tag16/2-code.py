import re   # import module "re" for using regex

my_search = re.search('a', 'Ham')   # a ist was ich in ham suche
print(my_search)   # span=1,2 

my_search = re.search('m', 'Ham')   # a ist was ich in ham suche
print(my_search)   # span=2, 3  




print()
print()
print('============== METACHARACTERS =============')
# . ^ $ * + ? {m}:


print('--- dot ---')
# dot - # The regex 'a.' matches the first 'a' character and any character after it
# a.  - gibt mit wo ein a mit irgendeinem anderen char als folge ist
# a.. - das gelcihe mit 2 chars als folge

match_obj = re.match('a.', 'abcdf')   #. --> the regex 'a.' with any char after this a (e.g. "ab")
print('a. -->', match_obj)


match_obj = re.match('a.', 'a')  # the regex "a." requires at least two char to amtch - so none
print('a. --> ', match_obj)





print()
print()
print('---- ^ caret ---')
# ^ caret  -  The regex '^a' matches the first character of the string 'abc'
# ^a  - wecher string startet mit einem a


match_obj = re.match('^a', 'abc') # wo startet string mit einem a
print(match_obj)

match_obj = re.match('^b', 'abc')   # none weil b nicht am anfang des strings
print('^b ---> ', match_obj)





print()
print()
print('---- $ ---')
# Dollar sign - 
# c$  - seeking for string that ends with e.g. c

match_obj = re.search('c$', 'abc')
print('c$--->abc ', match_obj)




print()
print()
print('---- * Asterisk---')
# The regex a* matches zer or more a char at ethe beginning of the string
# a* wie aaa

match_obj = re.match('a*', 'aaa')    
print('a* ---> aaa', match_obj)

match_obj = re.match('a*', 'baaa')   
print('a* ---> baaa', match_obj)


match_obj = re.match('a*', 'bbb')
print('a*---> bbb', match_obj)      # keine a's zu finden




print()
print()
print('---- + sign ---')
# such nach a+  einem oder merhreren a's am anfang eines strings

match_obj = re.match('a+', 'aaa')
print('a+ ---> aaa', match_obj)

match_obj = re.match('a+', 'bbb')
print('a+ ---> bbb', match_obj)    # none, es ist kein a 




print()
print()
print('----   ---')
# {m}
# 
match_obj = re.match('a{2}', 'aaa')
print(f'a{2} ---> aaa', match_obj)

# {m, n}
# mschaut wo zb aa und wo aaa sind 
match_obj = re.match('a{2,4}', 'aabaaaa')  
print(f'a{2,4} ---> aaaaa', match_obj)     



print()
print()
print('====== SPECTIAL SEQUENCES======')
print()
print()

print()
print('---- Character classes  ---')

print('---- \d ----')
# \d   - gibt uns string digits 0-9
match_obj = re.match('\d', '123')
print("\d ---> 123", match_obj)    # gibt mit 1 digit -> 1

match_obj = re.match('\d.', '123')              
print("\d ---> 123", match_obj)    # gibt mir 2 digits -> 12

match_obj = re.match('\d+', '123')
print("\d+ ---> 123", match_obj)   # gibt mit alle digits -> 123

match_obj = re.match('\d+', 'abc')
print("\d+ ---> abc", match_obj)   # gibt mit none weil:




match_obj = re.match('\s', 'hello')
print("\s ---> 'hello'", match_obj)   # 

match_obj = re.match('\w', 'hello')
print("\w ---> 'hello'", match_obj)   # 


match_obj = re.match('\w+', 'hello')
print("\w ---> hello", match_obj)   # 

match_obj = re.match('[abc]', 'alpha')
print("[abc] ---> alpha", match_obj)   # findet das a mit dem alpha beginnt



match_obj = re.match('[a-z]+', 'alpha')  # das + sagt: so lang du kannst sozusagen
print("[a-z]+ ---> a1lpha", match_obj)   # man bekommt das ganze alpha weil alles in a-z entahlen ist

match_obj = re.match('[a-z]+', 'a2lpha')
print("[a-z]+ ---> a1lpha", match_obj)   # man bekommt das a nur weil alpha mit a beginnt danach aber 2

match_obj = re.match('[a-zP]+', 'alPha')  # a-z UND ein großes P
print("[a-zP]+ ---> alpha", match_obj)   # man bekommt das ganze alphabet weil alles in alpha entahlen ist

match_obj = re.match('[a-zA-Z]+', 'alPha')  # a-z UND A-Z


match_obj = re.match('[^P]+', 'alPha1')  # alles  außer P
print("[^P]+ ---> alPha1", match_obj)   # daher gibt es alles bis zum P aus

print()
print()


pattern = '[xyz]'
text1 = 'hello xyz world'
matches = re.findall(pattern, text1) # überall wo er x,y oder z findet , packt er in eine liste
print("[xyz] --> hello xyz world", matches)  # ich habe nun x  y   und z gefunden im string

print()
print()

pattern = 'xyz'         # sucht nach dem string xyz
matches = re.findall(pattern, text1)
print("xyz --> hello xyz world: ", matches)   # ja, 'xyz' gefunden

matches = re.findall('xyz', 'hello xyz world')  # geht auch mit 2 strings als argument
print("xyz --> hello xyz world: ", matches)   # ja, 'xyz' gefunden


print()
print()
print('---- repetition characters  ---')
print()
print()

pattern = 'l+'  # gibt mir alle l+ in eine liste , also mindestens ein l 
matches = re.findall(pattern, text1)
print('l+ --> hello xyz world', matches)    #- zuerst die ll dann l


pattern = 'l?'  # gibt mir liste mit strings aus, die alle leere strings sind bis auf die stellen wo ein l ist
matches = re.findall(pattern, text1)
print('l? --> hello xyz world', matches) 



print('------groups------')

input_str = "John Smith, 25 years old"
pattern = "(\w+)\s(\w)" 
output_str = re.findall(pattern, input_str)
print('(\w+)\s(\w)) --> john smith, 25 years old', output_str)