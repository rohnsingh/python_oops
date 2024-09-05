from Item import Item
from Phone import Phone



item1 = Item("MyItem", 750)

# Setting an Attribute
Item.instantiate_from_csv()

# Getting an Attribute
print(item1.name)
print(Item.all)