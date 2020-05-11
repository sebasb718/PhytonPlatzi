def run():
  counter = 0
  with open("aleph.txt", "r", encoding="utf-8") as f:
    for line in f:
      counter += line.count("Beatriz")
  print("Beatriz está {} veces en el texto".format(counter))

if __name__ == "__main__":
  run()