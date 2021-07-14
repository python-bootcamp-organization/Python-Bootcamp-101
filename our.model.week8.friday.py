# import necessary functions
from IPython.display import clear_output
# global list variable
cart = []

# create function to add items to cart
def addItem(item):
    clear_output()
    cart.append(item)
    print( "{} has been added.".format(item) )

# create fuction to remove items from cart
def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print("{} has been removed.".format(item))
    except:
        print("Sorry we could not remove that item")

# create a fuction to show items in cart
def showCart():
    clear_output()
    if cart:
        print("Here is your cart:")
        for item in cart:
            print("- {}".format(item))
    else:
        print("Your cart is empty")

# create function to clear items from cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is empty.")

# create fuction to save items from cart
def saveCart():
    clear_output()
    f = open("saved_cart.txt", "w+")
    for item in cart:
        f.write("- {} \n".format(item))
    f.close()  
    print("Your requirs is saved.")