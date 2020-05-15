
def run():
  maxValue = int(input("Digite el valor maximo: "))
  suma = 0
  for i in range(0, maxValue + 1):
    suma = suma + i

  print("La suma recursiva es {}".format(suma))

if __name__ == "__main__":
  run()