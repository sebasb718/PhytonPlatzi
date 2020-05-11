def run():
  word = input("escriba la palabra ")
  if (word == word[::-1]):
    print("La palabra {} es palindromo".format(word))
  else:
    print("La palabra {} NO es palindromo".format(word))



if __name__ == "__main__":
  run()