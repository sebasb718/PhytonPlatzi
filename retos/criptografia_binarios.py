KEY = {
  'a': '00001010',
  'b': '00001011',
  'c': '00001100',
  'd': '00001101',
  'e': '00001110',
  'f': '00001111',
  'g': '00010000',
  'h': '00010001',
  'i': '00010010',
  'j': '00010011',
  'k': '00010100',
  'l': '00010101',
  'm': '00010110',
  'n': '00010111',
  'ñ': '00011000', 
  'o': '00011001',
  'p': '00011010', 
  'q': '00011011',
  'r': '00011100',
  's': '00011101',
  't': '00011110',
  'u': '00011111',
  'v': '00100000',
  'x': '00100001',
  'w': '00100010',
  'y': '00100011',
  'z': '00100100',
  ' ': '00100101'}

def encrypt(message):
  encryption = ""
  for i in message:
    encryption += KEY[i]
  return encryption

def decrypt(message):
  decryption = ""
  words = len(message) / 8
  start = 0
  end = 0
  for i in range(0, int(words)):
    end = start + 8
    messageValue = message[start:end]
    for key,value in KEY.items():
      if(value == messageValue):
        decryption += key
        start = end
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