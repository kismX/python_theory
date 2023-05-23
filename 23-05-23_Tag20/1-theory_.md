**Function day 2**
## Scope

- scope refers to the region of a prog whre a particular var is accessable

- var can be def in two different scopes
1. global
2. local

**global scopes**
- a var def outdise any func is said to be in the global scope
- global var acn be accessed from anywhere within the program.

**Local Scopes**
- var thar is defined in a func is said to be in the local scope.
- local var can only be accessed from within wht func in which they are def


**global vs. Local scope**
- when var is def both globally and locally, the local var takes precedence over the global var.


**scopes and variable lifespan**
- the lifespan of var is determined by its scope
- global var exist for the entire duration of the program
- local var only exist for the duration of their enclosing func


**passing different scope variables to a function:**
- 



## Names, Objects, Values
- in Py., everything is an object, whether it is a number, string, list, or even a func
- an object is a piece of memory that contains both:
1. data (the value of the object)
2. metadata (info about the object, such as its type and methods)

- every object in py has a unique identifier, which is a number that is assigned ot the object
- this  identifier can be obtained using the built-in **id()** func
- the identifier is quatranteed to be unige for the lifetime of the object

- a var in py is simply a name that refers to an object
- when a var is assigned a value, py creates an object for that value, and then binds the var to that object
- this means that the var is simply a reference or a pointer to the object, rather than the object itself

### Functions parameters as reference
- the only method of par passing in py is *cal by sharing*
- call by sharing means thatr each formal par of the func gets a copy of each reference in the args
- the result is that a func may chance any mutable object passed as par, but it cannot change the identity of those objects



- a popular way of explaining how par passing works in py is the phrase: "par are passed by value, but the values are references"
- in py the func gehts a copy of the argfs, but the args are always references.
- so the value of the referenced objectrs may be changed, if they are mutable, but their identity cannot

- *pass by sharing*
- *pass by object*