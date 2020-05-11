import random

def randomArray(arrayLength):
  array = []
  for i in range(arrayLength):
    array.append(random.randint(0,100))
  return array

def findByBinarySearch(array, number):
  print("Finding number {} in {}".format(number, array))
  array.sort()
  print("Sorted array {}".format(array))
  tries = 0
  low = 0
  high = len(array) - 1
  while True:
    tries += 1
    mid = int((high + low) / 2)
    if (array[mid] == number):
      index = array.index(number)
      print("Number found in index {} in {} tries".format(index,tries))
      break
    elif (array[mid] > number):
      high = mid - 1
    else:
      low = mid + 1

def run():
  arrayLenght = random.randint(1,20)
  array = randomArray(arrayLenght)
  numberToFind = array[random.randint(0, arrayLenght - 1)]
  findByBinarySearch(array,numberToFind)

if __name__ == "__main__":
  run()