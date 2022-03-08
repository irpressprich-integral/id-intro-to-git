animal = input("What animal are you?: ")

if animal == "":
   print("No input! Exiting...")
   exit()

print(f"What does the {animal} say?")

if animal == "cow":
   print("moo")
elif animal == "duck":
   print("quack")
elif animal == "chicken":
   print("cluck")
else:
   print("I don't know that one...")
