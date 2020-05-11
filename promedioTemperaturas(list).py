def run():
  temps = [20,30,25,22,21]
  suma = 0
  for i in temps:
    suma += i
  promedio = suma / len(temps)
  print("el promedio es {}".format(promedio))



if __name__ == "__main__":
  run()