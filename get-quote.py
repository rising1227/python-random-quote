import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  a = random.randint(0,last)
  print(quotes[a])

if __name__== "__main__":
  primary()
