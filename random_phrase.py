from time import sleep
import datetime

random_phrases = ["hola", "kha", "me", "llamo", "saitama", "por que", "es cierto", "wooo", "adios"]
large_phrases = [2,3,5,4,1,6,0,7,9,8]

for i in large_phrases:
    sleep(3)
    print(random_phrases[i])