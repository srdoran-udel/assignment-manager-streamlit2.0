import uuid
from typing import Optional, List, Dict


#query 1: place a new order for an item and quantity

#find orders placed for an inventory item using item id 

#step 2: find how many orders placed for the item using item id 

#find item information in inventory 


def place_order(inventory: list, orders: list, item_id: str, quantity: int) -> Optional[Dict]:
    item = find_inventory_item_by_item_id(inventory, item_id)
    #find item in inventory 
    #check if it exists ->
    if item: 
        if item['stock'] >= quantity:
            item['stock'] = item['stock'] - quantity
            total_cost = item['unit_price'] * quantity 
    #check if the stock is greater than the quantity
    #reduce inventory
    #then place the new order 
            new_order = { "order_id": str(uuid.uuid4()),
                         "item_id": item_id,
                         "quantity": quantity,
                         "status": "placed",
                         "total_cost": total_cost}
            orders.append(new_order)
            return new_order
     

def find_inventory_item_by_item_id(inventory: list, item_id: str) -> Optional[Dict]:
    for item in inventory:
        if item['item_id'] == item_id:
            return item     
    return []
        
    

def update_order_status():
    pass

def cancel_order():
    pass

def count_orders_for_item_by_item_id():
    pass