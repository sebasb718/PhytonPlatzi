"""
"abacabad" c
"abacabaabacaba" _
"abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" d
"bcccccccccccccyb" y

"""
def findFirstNonRepeatedCharacter(characters):
  characterCount = {characters[0]:1}
  for char in characters:
    if char not in characterCount:
      characterCount[char] = 1
    else:
      characterCount[char] += 1
  
  index = -1
  for key,value in characterCount.items():
    if value == 1 and index == -1 :
      index = characters.index(key)
    if characters.index(key) < index:
      index = characters.index(key)
  
  if index == -1:
    return ("_")
  else:
    return (characters[index])

def run():
  characters = "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe"
  result = findFirstNonRepeatedCharacter(characters)
  print(result)

if __name__ == "__main__":
  run()