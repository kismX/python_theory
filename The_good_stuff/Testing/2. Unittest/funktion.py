# ich nutze ein programm, dass man gut testen kan, bspw ein fibonacciprogramm, was wir oft hatten und auch oft genutzt wird (auch in interviews)

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a



