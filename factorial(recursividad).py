def run():
  number = int(input("Digite el numero que desea obtener el factorial "))
  print("El factorial de {} es {}".format(number,factorial(number)))

def factorial(number):
  if (number == 0):
    return 1
  else:
    return number * factorial(number - 1)

if __name__ == "__main__":
  run()