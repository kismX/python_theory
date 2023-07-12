import turtle

#Fenster einrichten
window = turtle.Screen()
window.bgcolor("skyblue")

#Turtle-Objekt erstellen
bird = turtle.Turtle()
bird.shape("turtle")
bird.color("black")

#Vogel zeichnen
bird.right(75)
bird.forward(100)
bird.left(150)
bird.forward(100)
bird.right(30)
bird.forward(70)
bird.left(120)
bird.forward(70)
bird.right(30)
bird.forward(100)

#Das Fenster offen halten
turtle.done()