# GENERA ALEATORIAMENTE LAS PALABARAS. EDITOR: DESDE MI PUNTO DE VISTA TOMAREMOS PALABRAS DE OTROS IDIOMAS, POR LO QUE EN UN FUTURO PROBABLEMENTE SEA ELIMINADO.
import random

Isolated = ["S","K","M","L","N","H","Y","E","W","I","O","A","T","D","R","Q","G","\""] # Letters at the beginning of words
Initials = ["S","K","M","L","N","H","Y","E","W","A","T","D","R","Q","G","\""] # Letters at the beginning of words
Medials = ["s","k","m","l","n","h","y","e","w","a","t","d","r","q","g","'"]   # Letters in the middle of words
Finals = ["s","k","m","l","n","h","e","i","o","a","t","d","r","q","g","'"]    # Letters at the ends of words

textLength = 500  # Number of words to generate

for i in range(1,textLength):
  num = int(min(10, max(1, random.gauss(5, 2))))  # Words with 5 letters are more common than shorter or greater.
  if num==1:
    string = random.choice(Isolated)
  else:
    string = random.choice(Initials)
    if num>1:
      for i in range(0,num-2):
        string += random.choice(Medials)
      string += random.choice(Finals)
    if random.random() > .85:  # 15% chance to add a period after each word.
      string += "."
  print(string, end=" ")
