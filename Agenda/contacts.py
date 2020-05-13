from contact import Contact
import csv

CONTACTS = {}

def run():
  while True:
    readFromFile("contacts.csv")

    value = input("""Digite la acción que quiere hacer:
    1 = añadir contacto
    2 = actualizar contacto
    3 = buscar contacto
    4 = eliminar contacto
    5 = mostrar todos contactos
    6 = salir 
    """)
    print("")

    if value == "1":
      print("Agregando un nuevo contacto")
      contact = getContactData()
      addContact(contact)
      writeToFile("contacts.csv")
    elif value == "2":
      print("Editando un contacto existente")
      newContact = getContactData()
      editContact(newContact)
      writeToFile("contacts.csv")
    elif value == "3":
      name = input("Escriba el nombre del contacto que desea buscar: ")
      if contactExist(name):
        showContact(CONTACTS[name])
      else:
        print("El contacto {} no existe".format(name))
    elif value == "4":
      name = input("Escriba el nombre del contacto que desea eliminar: ")
      deleteContact(name)
      writeToFile("contacts.csv")
    elif value == "5":
      for x in CONTACTS:
        showContact(CONTACTS[x])
    elif value == "6":
      print("Gracias por venir :)")
      break
    else:
      print("Comando no existe")

    print("")

def readFromFile(fileName):
  f = open(fileName, "r")
  r = csv.reader(f, delimiter=',')
  for row in r:
    CONTACTS[row[0]] = Contact(row[1], row[2], row[3])
  f.close()

def writeToFile(fileName):
  f = open(fileName, "w")
  w = csv.writer(f)
  for key, val in CONTACTS.items():
    w.writerow([key, val.name, val.email, val.phonenumber])
  f.close()

def deleteContact(name):
  if contactExist(name):
    CONTACTS.pop(name)
    print("Contacto eliminado")
  else:
    print("El contacto {} no existe".format(name))

def showContact(contact):
  print("---------------------------------------------")
  print("Nombre: {}".format(contact.name))
  print("Email: {}".format(contact.email))
  print("Telefono: {}".format(contact.phonenumber))
  print("---------------------------------------------")

def contactExist(name):
  if name in CONTACTS:
    return True
  else:
    return False

def editContact(newContact):
  if contactExist(newContact.name):
    CONTACTS[newContact.name] = newContact
    print("Contacto editado")
  else:
    print("El contacto {} no existe".format(newContact.name))

def getContactData():
  name = input("Escriba el nombre del contacto: ")
  email = input("Escriba el email del contacto: ")
  phoneNumber = input("Escriba el telefono del contacto: ")        
  return Contact(name, email, phoneNumber)

def addContact(contact):
  if contactExist(contact.name):
    print("El contacto {} ya existe".format(contact.name))
  else:
    CONTACTS[contact.name] = contact
    print("Contacto agregado")

if __name__ == "__main__":
  run()