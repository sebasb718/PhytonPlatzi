import random

def run():
  RandomNumber = random.randint(0,10)
  number = -1
  while number != RandomNumber:
    number = int(input("Escriba el numero "))
  
  print("Adivino el numero {}".format(RandomNumber))



if __name__ == "__main__":
  run()