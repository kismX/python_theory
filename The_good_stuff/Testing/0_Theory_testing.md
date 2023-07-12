### Unitest
1. was ist Unittest?
- unittest ist ein modul, welches tests beinhaltet, die man auf seine Programme anwenden kann. diese werden extern ausgeführt und nicht in deinem programmcode integriert.
- vorteil: test und code voneinander getrennt  /  nachtteil: aufwändiger
- und die darin enthaltene class TestCase enthält verschiedene methoden zum testen:


2. Anwenden
- du hast ein modul zb "funktion.py" erstellt mit einem Programm, z.b. fib() , das du testen möchtest
- nun erstellst du eine neue datei zb "funktion_unittest.py" 
    - importiere "unittest"    import unittest
    - importiere dein modul:   from funktion import fib
    - erstelle eine class mit beliebigem namen, die aus "TestCase" aus dem Modul "unittest" erbt
    - die methods, die du in deiner class für die testfälle programmiert können beliebig heißen, müssen aber mit "test" beginnen: zb: test_Fib
    - du wendest mit self einen der methods aus TestCase an.. zb self.assertEqual(a, b)   -> siehe TestCase Methoden weiter unten unter 3. 

3. TestCase Methoden
- setUp()
- tearDown()
- assertEqual(a, b, msg=None)    // dieser testcase testet die gleichheit des values eines arguments a mit dem erwarteten value b
                                    du kannst als argument a auch eine funktion einfügen: assertEqual(func(3), b)
                                    wenn du den default von msg = "blabla" änderst, gibt es dir im fehlerfall das "blabla" aus            
    - assertAlmostEqual()
    - assertCountEqual()
    - assertDictEqual()
- assertTrue()
- assertFalse()
- assertGreater()
- assertGreaterEqual()
- assertLess()
- assertLessEqual()
- assertIn()
- ...




### Pytest 
1. was ist pytest? 
-

2. was kann Pytest

3. Anwendung:
- zuerst installieren von pytest:   pip install -U pytest
- dann schau mal, welche version du installiert hast:   pytest --version
- um ein modul mit pytest zu prüfen, folgender code ins Terminal:   pytest -v test_name.py