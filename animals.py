animal = input("What animal are you?: ")

if animal == "":
   print("No input! Exiting...")
   exit()

print(f"What does the {animal} say?")

if animal == "lion":
   print("Roar!")
elif animal == "elephant":
   print("Toot")
elif animal == "leopard":
   print("Auuuff")
else:
   print("I don't know that one...")
