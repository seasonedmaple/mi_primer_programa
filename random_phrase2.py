from time import sleep
import datetime

happy_phrases = ["buenos dias", "que te vaya bien en tu dia"]
forniture_phrases = ["silla", "mesa"]
drink_phrases = ["tonayan", "four loko"]
hater_phrases = ["pendejo", "eres tonto "]
forniture_phrases = ["tortas", "chile en nogada"]
absurd_phrases = ["me gusta comer pasto", "soy un bebe"]
animal_phrases = ["león ", "elefante"]
motivational_phrases = ["los obstaculos son herramientas para el exito", "preferirias estar muerto a ser un perdedor"]
sounds_animal_phrases = ["miau", "woof"]
sad_phrases = ["somos un parapadeo en la vida del universo", "podemos usar el tiempo, pero no nos pertenece"]

large_phrases = [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20]
current_second = 0

for i in large_phrases:
    if current_second == 0:
        sleep(1)
        print(happy_phrases[i])
        current_second += 1
    return current_second
