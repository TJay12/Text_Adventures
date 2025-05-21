from data.shops import shops_inventory
from character import inventory
from character import add_to_inventory

#----------------------------------------------------------------------------------------------   <---Shop Functions--->
# <---View Shop---> ----------------------------------------------------------------------------------------------------
def view_shop():
    for item, data in shops_inventory.items():
        value = data["value"]
        in_stock = data["in_stock"]
        print(f"{item}: {value} coins ({in_stock} in stock)")

# <---Buy from Shop---> ------------------------------------------------------------------------------------------------
def buy_items():
    buying = input("What would you like to buy? ")
    if buying not in shops_inventory:
        print("That item doesn't exist in shop")

    try:
        quantity = int(input("How many? "))
    except ValueError:
        print("Please enter a numerical value")
        return

    item_data = shops_inventory[buying]
    value = item_data["value"]
    in_stock = item_data["in_stock"]
    total_cost = value * quantity

    if in_stock < quantity:
        print("The shop doesn't have that many items in stock")
    elif inventory["coins"] < total_cost:
        print("You dont have enough coins for this purchase")
    else:
        inventory["coins"] -= total_cost
        item_data[in_stock] -= quantity
        add_to_inventory(buying, quantity)
        print(f"You bought {quantity} {buying} for {total_cost} coins")

# <---Sell to shop--> --------------------------------------------------------------------------------------------------
def sell_items ():
    selling = input("What would you like to sell? ")
    if selling not in shops_inventory:
        print("That item doesn't exist in shop")
    else:
        try:
            quantity = int(input("How many? "))
        except ValueError:
            print("Please enter a numerical value")
            return

        if quantity <= inventory[selling] :
            inventory[selling] -= quantity
            inventory["coins"] += inventory[selling] * quantity
        else:
            print("Not enough items for sale")