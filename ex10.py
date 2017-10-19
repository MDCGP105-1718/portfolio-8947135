y = int(input("Specificate a low value : "))
z = int(input("Specificate a high value : "))
Count = range(y,z)
def FizzBuzz(x) :
    for x in range (y,z) :
     if x % 3 == 0 :
      print("Fizz")
     elif x % 5 == 0 :
      print("Buzz")
     elif x % 3 == 0 and x % 5 == 0 :
      print ("FizzBuzz")
     else :
      print(x)

FizzBuzz(Count)
