while True:
  a = input("Enter the temperature in degree celcius that you want to convert in degree farhenheit (Enter q to quit): ")
  if str(a).lower()=="q":
    break
  a = int(a)
  frt = (9/5)*a + 32
  print("Your Temperature in degree farhenheit is: ",frt)
