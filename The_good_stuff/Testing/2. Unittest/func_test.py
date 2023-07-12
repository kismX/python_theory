#du importierst das moful, in welchem die tests enthalten sind
import unittest     

#du importierst dein programm, welches du testen möchtest
from funktion import fib

#erstellen einer class mit indiv. namen, welche aus dem Modul TestCase erbt, um die Tests verfügbar zu machen
class FibTest(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(0), 0)   #ich wähle assertEqual, um die func mit arg mit dem erwarteten ergebnis zu vergleichen
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)


# hmmmmmm 
if __name__ == "__main__":
    unittest.main()



## nun kannst du in der konsole den oben programmierten testfall aufrufen:
#    python3 func_test-py   oder du klickt auf den RUN-Button :D
## wenn du pytest installiert hast, kannst du den test damita usführen, ins terminal:    pytest -v func_test.py



