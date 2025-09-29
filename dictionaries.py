# Its a menu program

cart = []
total = 0

print("--------- menu ---------")
menu = {"hot dog": 3.50,
        "hamburger": 4.00,
        "soda": 1.50,
        "chips": 1.00,
        "candy": 1.25,
        "chocolate bar": 1.75}

for key,value in menu.items():
    print(f"{key:15} : ${value:.2f}")
print("------------------------")


while True:
    item = input("enter the item you want to buy (or q to quit): ").lower()
    if item == "q":
        break
    elif menu.get(item) is not None :
        cart.append(item)

print("-------- your cart ---------")        
for item in cart:
    total += menu.get(item)
    print(item,end= " ")
print()    
print(f"your total is : ${total:.2f}")






    