
def run():
  print("Tu número es primo? ")
  number = int(input("Digite el numero: "))
  if(isPrime(number)):
    print("El número {} es primo".format(number))
  else:
    print("El número {} no es primo".format(number))

def isPrime(number):
  for i in range(number):
    i = i + 1
    if(i != 1 and i != number and number % i == 0):
      return False
  return True

if __name__ == "__main__":
  run()
