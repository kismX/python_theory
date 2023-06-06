# Logical Thinking

- Truth Tables
- Truthy and falsy values
- short circuiting

<< Table in piets md>>



## Truth Tables
**AND** 
True + True = True
true + False = False
Fals + False = False

**OR**
einer der zustände muss true sein, dann ist es true


**NOT**
true ist false und flase ist true


**XOR: !=**
True, wenn eines der zustände unterschiedlich ist (false != true = True)


**NAND: Not AND**
False wenn alle zustände true sind, sobald einer False, dann true


**NOR: not (A or B)**
True, wenn alle zustände False sind.. sonst False


**XNOR: A==B**
immer true wenn alle zustände entweder True oder alle zustände False sind True + true = True .. FAlse + False = True


**Truthy ans FFalsy valuies**
- wenn element leer ist ( z.B. x = [] ) dann ist kein Wert enthalten udn es ist Falsy
- alles was inhalt hat ist Truthy

# Beispiele:
- true:  truthy
- 1: Truthy
- False: falsy
- 0: Falsy
- x = "String": truthy
- x = []: falsy
- x = {}: Falsy
- x = [1,2,3]: truthy
- None: Falsy

## Predicate
- p are statemenmts that can be either true or false
1. comparison p.: ==   !=   >   >
2. membership p.: 2 in [1,2,3]    3 in [1,2]   3 not in [1,2]
3. identity p: check if values or expressions refer to the same object in memory
4. BNoolean p.: combine other (..siehe peit)

## Evaluation Precedence
order in which operatirs and ecxpressions are evaluated in an expression
in py the order of operator prec. is as follows (from highest to lowest):
1. parantheses - klammern gehen vor
2. ecponentiation - hochzahlen gehen danach vor
3. multiplicartion/divisoin/flor division
4. addition and substraction (+ - )
5. comparison operator (< > <= == !=)
6. boolean operators (not and or) 

# naming and grouping p.
def a func that takes one or more args and returns a bool