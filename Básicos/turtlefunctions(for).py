import turtle

def main():
  window = turtle.Screen()
  sebas = turtle.Turtle()
  makeSquare(sebas)

def makeSquare(turtle):
  lenght = int(input("Digite el largo y presione enter: "))
  for i in range(4):
    makeLineAndTurn(turtle, lenght)
  input()

def makeLineAndTurn(turtle, lenght):
  turtle.forward(lenght)
  turtle.left(90)

if __name__ == '__main__':
  main() 