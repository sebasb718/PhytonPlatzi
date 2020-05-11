KEY = {
  'a': 'w',
  'b': 'E',
  'c': 'x',
  'd': '1',
  'e': 'a',
  'f': 't',
  'g': '0',
  'h': 'C',
  'i': 'b',
  'j': '!',
  'k': 'z',
  'l': '8',
  'm': 'M',
  'n': 'I',
  'o': 'd',
  'p': '.',
  'q': 'U',
  'r': 'Y',
  's': 'i',
  't': '3',
  'u': ',',
  'v': 'J',
  'w': 'N',
  'x': 'f',
  'y': 'm',
  'z': 'W',
  'A': 'G',
  'B': 'S',
  'C': 'j',
  'D': 'n',
  'E': 's',
  'F': 'Q',
  'G': 'o',
  'H': 'e',
  'I': 'u',
  'J': 'g',
  'K': '2',
  'L': '9',
  'M': 'A',
  'N': '5',
  'O': '4',
  'P': '?',
  'Q': 'c',
  'R': 'r',
  'S': 'O',
  'T': 'P',
  'U': 'h',
  'V': '6',
  'W': 'q',
  'X': 'H',
  'Y': 'R',
  'Z': 'l',
  '0': 'k',
  '1': '7',
  '2': 'X',
  '3': 'L',
  '4': 'p',
  '5': 'v',
  '6': 'T',
  '7': 'V',
  '8': 'y',
  '9': 'K',
  '.': 'Z',
  ',': 'D',
  '?': 'F',
  ' ': ' ',
  '!': 'B'
}

def encrypt(message):
  encryption = ""
  for i in message:
    encryption += KEY[i]
  return encryption

def decrypt(message):
  decryption = ""
  for i in message:
    for key,value in KEY.items():
      if(value == i):
        decryption += key
        break
  return decryption

def run():
  while True:
    print("")
    print("Criptografo")
    print("¿Que desea hacer?")
    print("Digite 1 para encriptar")
    print("Digite 2 para desencriptar")
    print("Digite 3 para salir")
    option = int(input())
    if(option == 1):
      message = input("Escriba el mensaje en encriptar: ")
      result = encrypt(message)
      print("El mensaje encriptado es: {}".format(result))
    elif (option == 2):
      message = input("Escriba el mensaje en encriptar: ")
      result = decrypt(message)
      print("El mensaje desencriptado es: {}".format(result))
    elif (option == 3):
      break
    else:
      print("Opción no valida")

if __name__ == "__main__":
  run()