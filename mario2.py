def main():
  while(True):
    n = int(input("N: "))
    if n >= 1 and n <= 8:
         break
  draw(n)

def draw(n):
    for i in range(n):
      print((n-i) * " " + i * "#" + '  ' *2 + "#" * i) 
main()
