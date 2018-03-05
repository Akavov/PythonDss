#kortej2
inventory=("sword",
           "armor",
           "shield",
           "hil potion")
print("\SO, in your arsenal:")
for item in inventory:
    print(item)
input("\nPress Enter to continue")
print("Now in your arsenal ",len(inventory)," things")
input("\nPress enter to continiue)

if "hil potion" in inventory:
      print("Long life to the King!")

index=int(input("\nPut index of thing from arsenal: "))
print("After index ",index," in arsenal is ",inventory[index]))
