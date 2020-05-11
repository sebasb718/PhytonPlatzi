from lamp import Lamp

def run():
  lamp = Lamp(is_turned_on = False)
  while True:
    command = input("Digite 1 para prender, 2 para apagar y 3 para salir: ")

    if command == "1":
      lamp.turn_on()
    elif command == "2":
      lamp.turn_off()
    else:
      break

if __name__ == "__main__":
  run()  
