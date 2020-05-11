def run():
  with open("numeros.txt", "w") as f:
    for number in range(0,10):
      f.write(str(number))

if __name__ == "__main__":
  run()