###     LAST MINUTE SELLING/BUYING PLATFORM     ###
 
# Code to simulate a platform where supermarket can sell something and other people can buy items.

# This program was repared for the course "30492 - Entrepreneurship and New Business Startup" at Bocconi University in which me and some colleagues 
# had to prepare a group project in which we created a startup. Me and my group worked on a last minute market where potential sellers can sell products 
# that are close to exipration date and potential buyers can buy any product.
# Among the course requisites there was the developement of a prototype of the project and this is the python code I developed for this purpose: 
# it is possible to simulate the buying/selling procedure in an interactive way in which each potential seller can register and put an item in the market 
# and each potential seller can pick a seller and buy an item from him.

# Datas of buyers and sellers are stored in dictionaries that are initialised, for simulating purposes, with some variables in them. 
# In particular, buyers is the dictionary of buyers that registered to the "platform" and each user has associated a list with entries 
# "numebrs of items bought" and "total points" associated to the users (he can use points to get further discounts). 

# Similarely, sellers is the dictionary of the shops who are selling: each shop has a dictionary associated to it and each key of the subdictionary 
# is a product that is on the market and it has list associated with NUMBER OF PRODUCTS, SELLING PRICE, ORIGINAL PRICE, DISCOUNT RATE, EXPIRATION DATE (in missing days) and TYPE OF PRODUCT.
# The code is interactive and the user (both buyer and saller) can answer to the proposed questions through the input() 
# function selecting their role, registering and then, based on the role, sell or buy something.

# The code is guided throug comments explainig what is done in each step.

# 1 FUNCTIONS

# 1.1 INITIALIZATION OF AUXILIARY FUNCTIONS AND VARIABLES

def market_matrix_function(sellers):
    # Matrix header
    market_matrix = [
        ["NAME OF SHOP", "OBJECT", "NUMBER", "SELLING PRICE", "ORIGINAL PRICE", "DISCOUNT RATE (%)", "EXPIRATION DATE (days)", "TYPE OF PRODUCT"],
    ]
    
    for shop_name, shop_products in sellers.items():
        if shop_products:  # Check if shop_products is non empty
            for product, characteristic in shop_products.items():
                market_matrix.extend([
                    [
                        shop_name,
                        product,
                        characteristic[0],  # NUMBER
                        characteristic[1],  # SELLING PRICE
                        characteristic[2],  # ORIGINAL PRICE
                        characteristic[3],  # DISCOUNT RATE (%)
                        characteristic[4],  # EXPIRATION DATE (days)
                        characteristic[5],  # TYPE OF PRODUCT
                    ]
                ])
        else:  # Add an empty row if no products
            market_matrix.append([shop_name] + [""] * 7)
    return market_matrix

# Dictionary of sellers. Each key of the dictionary is a shop and each shop has a subdictionary in which the keys are the products.
# Each pruduct has a list associated with the values relative to NUMBER, SELLING PRICE, ORIGINAL PRICE, DISCOUNT RATE (%), EXPIRATION DATE (days), TYPE OF PRODUCT.

sellers = {
    "ESSELUNGA": {
        "BANANA": [4, 1, 2.5, (1 - 1 / 2.5), 7, "FRUIT"],
        "BREAD": [3, 2, 2.5, round((1 - 2 / 2.5), 2), 1, "BAKERY"]
    },
    "COOP": {
        "APPLE": [3, 1, 2.5, (1 - 1 / 2.5), 1, "FRUIT"],
    },
    "LIDL": {
        "BANANA": [2, 1, 2.5, (1 - 1 / 2.5), 1, "FRUIT"],
        "BREAD": [2, 1, 2.5, (1 - 1 / 2.5), 1, "BAKERY"],
        "APPLE": [2, 1, 2.5, (1 - 1 / 2.5), 1, "FRUIT"],
    }
}

# create the matrix of the market with the function market_matrix_function dove before
market_matrix = market_matrix_function(sellers)

market_matrix

# function to print the matrix in a readible way
def print_market(market_matrix):
    width_of_printed_column = [max(len(str(item)) for item in column_of_matrix) for column_of_matrix in zip(*market_matrix)]
    for row in market_matrix:
        print("| " + " | ".join(f"{str(item):<{width}}" for item, width in zip(row, width_of_printed_column)) + " |")

print_market(market_matrix)

# Dictionary of buyers. Each key of the dictionary is a buyer and each buyer has a list associated with the values relative to NUMBER OF BOUGHT ITEMS and POINTS.
buyers = {
    # NAME: [NUMBER OF BOUGHT ITEMS, POINTS]
    "ALEX": [3, 12], 
    "JAMES": [2, 5],
}


# 1.2 SELLER PART FUNCTIONS

def seller_function():
    
    # Question to the seller if the seller is already registered. 
    # In case YES, go to the next step. In case NO, ask if the seller wants to register.
    seller_registered_question_seller = input("Are you altraedy registered?\nType Y for YES and N for NO").upper().strip()
    while seller_registered_question_seller not in ["Y", "N"]:
        seller_registered_question_seller = input("Give valid answer (Y or N)").upper().strip()

    # If the answer is YES (it is already registered), ask the name of the seller and check if the name is in the dictionary of sellers.
    if seller_registered_question_seller == "Y":
        ask_name_seller = input("What is your name?").upper().strip()
        while (ask_name_seller.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == ""):
            ask_name_seller = input("Either you gave an unvalid string or this name is already used. Please try again.").upper().strip()

        # If the name is not in the dictionary of sellers (he is not registered), ask if the seller wants to register.
        if ask_name_seller not in sellers:
            new_seller_registered_question_seller = input("You are not registered. Do you want to register?\nType Y for YES and N for NO").upper().strip()
            while new_seller_registered_question_seller not in ["Y", "N"]:
                new_seller_registered_question_seller = input("Give valid answer (Y or N)").upper().strip()
            
            # If the answer is YES (he wants to register), ask the name of the seller and then go to the next step (selling procedure).
            if new_seller_registered_question_seller == "Y":
                ask_name_seller = input("What is your name for registration?").upper().strip()
                while (ask_name_seller.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == "") or (ask_name_seller in sellers): 
                    ask_name_seller = input("Either you gave an unvalid string or this name is already used. Please try again.").upper().strip()

                sellers[ask_name_seller] = {}
                print("You are registered now.")
                return want_to_sell_function(ask_name_seller)
            
            # If the answer is NO (he does not want to register), the seller can not sell anything and code ends.
            if new_seller_registered_question_seller == "N":
                print("You can not sell anything without registration.")
                pass

        # If the name is in the dictionary of sellers (he is registered), go to the next step (selling procedure).
        if ask_name_seller in sellers:
            return want_to_sell_function(ask_name_seller)

    # If the answer is NO (it is not already registered), ask if the seller wants to register.
    if seller_registered_question_seller == "N":
        new_seller_registered_question_seller_2 = input("Do you want to register?\nType Y for YES and N for NO").upper().strip()
        while new_seller_registered_question_seller_2 not in ["Y", "N"]:
            new_seller_registered_question_seller_2 = input("Give valid answer (Y or N)").upper().strip()
        
        # If the answer is YES (he/she wants to register), ask the name of the seller and check if the name is in the dictionary of sellers
        if new_seller_registered_question_seller_2 == "Y":
            ask_name_seller_2 = input("What is your name for registration?").upper().strip()
            while (ask_name_seller_2.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == "") or (ask_name_seller_2 in sellers): 
                ask_name_seller_2 = input("Either you gave an unvalid string or this name is already used. Please try again.").upper().strip()

            sellers[ask_name_seller_2] = {}
            return want_to_sell_function(ask_name_seller_2)
        
        # If the answer is NO (he/she do not want to register), the seller can not sell anything and code ends.
        if new_seller_registered_question_seller_2 == "N":
            print("You can not sell anything without registration.")
            pass

def want_to_sell_function(name_of_seller):
    # Start the selling procedure.
    # Ask the seller if he/she wants to sell something.
    want_to_sell = input("Do you want to sell something?\nType Y for YES and N for NO").upper().strip()
    while want_to_sell not in ["Y", "N"]:
        want_to_sell = input("Give valid answer (Y or N)").upper().strip()

    # If the answer is NO (he/she does not want to sell), the seller can not sell anything and code ends.
    if want_to_sell == "N":
        return print("You are not selling anything.")
    
    # If the answer is YES (he/she wants to sell), ask the seller informations of the product he wants to sell.
    # Checks of types of the inputs are done in the functions get_number, get_product_price, get_selling_price, get_date written below.
    if want_to_sell == "Y":
        # ask name of the product
        product_name = input("What is the name of the product you want to sell?").upper().strip()
        while (product_name.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == "") or (product_name in sellers[name_of_seller]):
            product_name = input("Either you give an unvalid string or you are already selling this product. Please try again.").upper().strip()

        # ask number of the product
        product_number = int(get_number())

        # ask price of the product
        product_original_price = round(float(get_product_price()), 2)

        # calculate the selling price and the discount rate
        product_selling_price = round(float(get_selling_price(product_original_price)), 2)

        # computation of the discount rate
        product_discount_rate = round((1-product_selling_price/product_original_price), 2)
        
        # ask the expiration date of the product
        product_expiration_date = int(get_date())

        # ask the type of the product
        product_type = input("What is the type of this product?").upper().strip()
        while (product_type.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == ""): 
            product_type = input("You gave an unvalid string. Please try again.").upper().strip()

        sellers[name_of_seller][product_name] = [product_number, product_selling_price, product_original_price, product_discount_rate, product_expiration_date, product_type]

        print(f"You are selling {product_number} units of {product_name} at the price of {product_selling_price}€ with a discount rate of {product_discount_rate*100}%," 
                     f"the expiration date is in {product_expiration_date} days.")
        
        print("\n\nNow the market looks like this:")
        market_matrix = market_matrix_function()
        print_market(market_matrix)


# Check if the input is a valid number (positive integer). If not, ask again.
def get_number():
    while True:
        number = input("How many units of this product do you want to sell?")
        try :
            number = int(number)
            if number > 0:
                return number
            else:
                print("Number of units must be positive")
        except ValueError:
            print("Give a valid number (positive integer)")


# Check if the input is a valid price (positive float). If not, ask again.
def get_product_price():
    while True:
        product_original_price = input("What is the original price of this product? ")
        try:
            # Try to convert the input to a float
            product_original_price = float(product_original_price)
            if product_original_price > 0:
                return product_original_price  # If successful, return the float value
            else:
                print("Price must be positive")
        except ValueError:
            # If conversion fails, print an error message and repeat the prompt
            print("Give a valid number (positive integer or float)")


# Check if the input is a valid price (positive float less than the original price of the product). If not, ask again.
def get_selling_price(product_original_price):
    while True:
        product_selling_price = input("What is the selling price of this product? ")
        try:
            # Try to convert the input to a float
            product_selling_price = float(product_selling_price)
            if product_selling_price <= product_original_price:
                return product_selling_price  # If successful, return the float value
            else:
                print("The selling price must be lower than the original price.")
        except ValueError:
            # If conversion fails, print an error message and repeat the prompt
            print(f"Give a valid number (positive integer or float less than {product_original_price})")


# Check if the input is a valid date (positive integer indicating missing days). If not, ask again.
def get_date():
    while True:
        number = input("How many days are miising to expiration?")
        try :
            number = int(number)
            if number > 0:
                return number
            else :
                print("The expiration date (in missing days) must be a positive integer.")
        except ValueError:
            print("Give a valid number (positive integer)")



# 1.3 BUYER PART FUNCTIONS

def buyer_function():

    # Question to the buyer if the buyer is already registered.
    # In case YES, go to the next step. In case NO, ask if the buyer wants to register.
    buyer_registered_question_buyer = input("Are you altraedy registered?\nType Y for YES and N for NO").upper().strip()
    while buyer_registered_question_buyer not in ["Y", "N"]:
        buyer_registered_question_buyer = input("Give valid answer (Y or N)").upper().strip()

    # If the answer is YES (it is already registered), ask the name of the buyer and check if the name is in the dictionary of buyers.
    if buyer_registered_question_buyer == "Y":
        ask_name_buyer = input("What is your name?").upper().strip()

        # If the name is not in the dictionary of buyers (he is not registered), ask if the buyer wants to register.
        if ask_name_buyer not in buyers:
            new_buyer_registered_question_buyer = input("You are not registered. Do you want to register? You will get 5 free points.\nType Y for YES and N for NO").upper().strip()
            while new_buyer_registered_question_buyer not in ["Y", "N"]:
                new_buyer_registered_question_buyer = input("Give valid answer (Y or N)").upper().strip()
            
            # If the answer is YES (he wants to register), ask the name of the buyer and then go to the next step (buying procedure).
            # Registering the buyer gets 5 free points.
            if new_buyer_registered_question_buyer == "Y":
                ask_name_buyer = input("What is your name for registration?").upper().strip()
                while (ask_name_buyer.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == "") or (ask_name_buyer in buyers): 
                    ask_name_buyer = input("Either you gave an unvalid string or this name is already used. Please try again.").upper().strip()

                buyers[ask_name_buyer] = [0, 5]
                print("You are registered now.")
                return want_to_buy_function(ask_name_buyer, sellers, buyers)
            
            # If the answer is NO (he does not want to register), the buyer can not buy anything and code ends.
            if new_buyer_registered_question_buyer == "N":
                print("You can not buy anything without registration.")
                pass

        # If the name is in the dictionary of buyers (he is registered), go to the next step (buying procedure).
        if ask_name_buyer in buyers:
            return want_to_buy_function(ask_name_buyer, sellers, buyers)
        
    # If the answer is NO (it is not already registered), ask if the buyer wants to register.
    if buyer_registered_question_buyer == "N":
        new_buyer_registered_question_buyer_2 = input("Do you want to register? You will get 5 extra points.\nType Y for YES and N for NO").upper().strip()
        while new_buyer_registered_question_buyer_2 not in ["Y", "N"]:
            new_buyer_registered_question_buyer_2 = input("Give valid answer (Y or N)").upper().strip()
        
        # If the answer is YES (he/she wants to register), ask the name of the buyer and then go to the next step (buying procedure).
        if new_buyer_registered_question_buyer_2 == "Y":
            ask_name_buyer_2 = input("What is your name for registration?").upper().strip()
            while (ask_name_buyer_2.replace(r"\N", "").replace("\T", "").replace("\R", "").strip() == "") or (ask_name_buyer_2 in buyers): 
                ask_name_buyer_2 = input("Either you gave an unvalid string or this name is already used. Please try again.").upper().strip()

            buyers[ask_name_buyer_2] = [0, 5]
            return want_to_buy_function(ask_name_buyer_2, sellers, buyers)
        
        # If the answer is NO (he/she do not want to register), the buyer can not buy anything and code ends.
        if new_buyer_registered_question_buyer_2 == "N":
            return print("You can not buy anything without registration.")


def want_to_buy_function(name_of_buyer, sellers, buyers):

    # Start the buying procedure.
    print("The market is:")
    market_matrix = market_matrix_function(sellers)
    print_market(market_matrix)
    list_of_sellers, list_of_products = [], []

    # Ask the buyer if he/she wants to buy something or if he wants to or if he wants to apply any filters to the market.
    want_to_buy = input("Do you want to buy something or see a filtered market?\nType Y for YES, N for NO or F for FILTERS").upper().strip()
    while want_to_buy not in ["Y", "N", "F"]:
        want_to_buy = input("Give valid answer (Y or N or F)").upper().strip()

    # If the answer is NO (he/she does not want to buy), the buyer do not want to buy anything and code ends.
    if want_to_buy == "N":
        return print("You are not buying anything.")
    
    # If the answer is YES (he/she wants to buy), ask the buyer informations of the product he wants to buy.
    # Checks on the inputs types are done in the functions choosen_number_function, min_price, max_price, min_days, max_days written below.
    if want_to_buy == "Y":
        for seller in sellers:
            list_of_sellers.append(seller)

        # Asking from which seller the buyer wants to buy and checking if the seller is in the market.
        choosen_seller = input(f"From which seller do you want to buy among {list_of_sellers}?").upper().strip()
        while choosen_seller not in sellers:
            choosen_seller = input(f"This seller is not in the market. Please give an other one among {list_of_sellers}.").upper().strip()
        
        # Preparation of a list with items on the market by such seller
        for product in sellers[choosen_seller]:
            list_of_products.append(product)

        # Given the choosen seller, ask to the buyer what he wants to buy and check if the product is in the market.
        choosen_object = input(f"What do you want to buy among {list_of_products}?").upper().strip()
        while choosen_object not in list_of_products:
            choosen_object = input(f"This object is not in the market. Please give an other one among {list_of_products}.").upper().strip()

        # Ask to the buyer how much of the product he wants to buy and check if the number is available in the market.
        choosen_number = int(choosen_number_function(sellers[choosen_seller][choosen_object][0]))
       
       # Computation of the price and of the points that the buyer can use to get a discount. 
       # Then ask if the buyer wants to use the points to get a discount.
        total_price = round(choosen_number * sellers[choosen_seller][choosen_object][1], 2)
        possible_points = buyers[name_of_buyer][1]
        max_points = min(possible_points, total_price/10)
        discount = max_points * 10
        discounted_price = total_price
        if possible_points > 0:
            input_points = input(f"You can use {max_points} points to get a discount of {discount}€. Do you want to use them? Type Y for YES and N for NO").upper().strip()
            while input_points not in ["Y", "N"]:
                input_points = input("Give valid answer (Y or N)").upper().strip()

            # If the answer is YES (he/she wants to use the points), compute the discounted price and update the number of points of the buyer.
            # If the answer is NO (he/she does not want to use the points), the price remains the same and the code is skipped.
            if input_points == "Y":
                discounted_price = round(total_price - max_points*0.1, 2)
                buyers[name_of_buyer][1] -= max_points


        # updating the number of bought items
        buyers[name_of_buyer][0] += choosen_number
        sellers[choosen_seller][choosen_object][0] -= choosen_number
        if sellers[choosen_seller][choosen_object][0] == 0:
            del sellers[choosen_seller][choosen_object]
            

    # If the answer is F (he/she wants to filter the market), ask the buyer how he/she wants to filter the market.
    if want_to_buy == "F":
        filtered_market = {}

        # Ask the buyer how he/she wants to filter the market (by price P, by type of product T or by missing days to expiration E).
        type_of_filter = input("Do you want to filter by PRICE or TYPE or MISSING DAYS TO EXPIRATION?\nType P for PRICE, T for Type or E for EXPIRATION").upper().strip()
        while type_of_filter not in ["P", "T", "E"]:
            type_of_filter = input("Give valid answer (P or T or E)").upper().strip()

        # If he wants to filter by price P, ask the buyer the minimum and maximum prices of the product he/she is looking for.
        if type_of_filter == "P":
            min_price = float(min_price())
            max_price = float(max_price(min_price))
            for seller in sellers:
                for product in sellers[seller]:
                    if sellers[seller][product][1] >= min_price and sellers[seller][product][1] <= max_price:
                        if seller not in filtered_market:
                            filtered_market[seller] = {}
                        filtered_market[seller][product] = sellers[seller][product]

        # If he wants to filter by type T, ask the buyer the type of the product he/she is looking for.
        if type_of_filter == "T":
            type_of_product = input("What is the type of the product you are looking for?").upper().strip()
            for seller in sellers:
                for product in sellers[seller]:
                    if sellers[seller][product][5] == type_of_product:
                        if seller not in filtered_market:
                            filtered_market[seller] = {}
                        filtered_market[seller][product] = sellers[seller][product]

        # If he wants to filter by missing days to expiration E, ask the buyer the minimum and maximum number of days to expiration of the product he/she is looking for.
        if type_of_filter == "E":
            min_days = int(min_days())
            max_days = int(max_days(min_days))
            for seller in sellers:
                for product in sellers[seller]:
                    if sellers[seller][product][4] >= min_days and sellers[seller][product][4] <= max_days:
                        if seller not in filtered_market:
                            filtered_market[seller] = {}
                        filtered_market[seller][product] = sellers[seller][product]

        print("The filtered market looks like this:")

        # Creation of filtered market matrix
        filtered_market_matrix = market_matrix_function(filtered_market)

        # Print the filtered market
        print_market(filtered_market_matrix)

        # Recursion to ask the buyer if he/she wants to buy something from the filtered market.
        return want_to_buy_function(name_of_buyer, filtered_market, buyers)

    
    return print(f"You bought {choosen_number} units of {choosen_object} from {choosen_seller} at the price of {discounted_price}€.")


# Check if the input is a valid number (positive integer). If not, ask again.
def choosen_number_function(max_number):
    while True:
        choosen_number = (input("How many units do you want to buy?"))
        try :
            choosen_number = int(choosen_number)
            if choosen_number > 0 and choosen_number <= max_number:
                return choosen_number
            else:
                print(f"Number of units must be an integer positive and lower than {max_number}.")
        except ValueError:
            print("Give a valid number (positive integer)")



# Check if the input is a valid price (positive float). If not, ask again.
def min_price():
    while True:
        min_price = input("What is the minimum price you want to pay?")
        try:
            min_price = float(min_price)
            if min_price > 0:
                return min_price
            else:
                print("Price must be positive")
        except ValueError:
            print("Give a valid number (positive integer or float)")


# Check if the input is a valid price (positive float higher than the minimum price). If not, ask again.
def max_price(min_price):
    while True:
        max_price = input("What is the maximum price you want to pay?")
        try:
            max_price = float(max_price)
            if max_price >= min_price:
                return max_price
            else:
                print("The maximum price must be higher than the minimum price.")
        except ValueError:
            print("Give a valid number (positive integer or float)")



# Check if the input is a valid number (positive integer). If not, ask again.
def min_days():
    while True:
        min_days = input("What is the minimum number of days to expiration you want?")
        try:
            min_days = int(min_days)
            if min_days > 0:
                return min_days
            else:
                print("The number of days must be positive")
        except ValueError:
            print("Give a valid number (positive integer)")


# Check if the input is a valid number (positive integer higher than the minimum number of days). If not, ask again.
def max_days(min_days):
    while True:
        max_days = input("What is the maximum number of days to expiration you want?")
        try:
            max_days = int(max_days)
            if max_days >= min_days:
                return max_days
            else:
                print("The maximum number of days must be higher than the minimum number of days.")
        except ValueError:
            print("Give a valid number (positive integer)")



# 2. START OF SIMULATION

# Ask to the user if he is a buyer or a seller and check if the answer is valid.
demand = input("Are you a BUYER (type B) or a SELLER (type S)?").upper().strip()
while demand not in ["B", "S"]:
    demand = input("give valid answer (B or S)").upper().strip()

# If the user is a buyer, go to the buyer functions.
if demand == "B":
    buyer_function()

# If the user is a seller, go to the seller functions.
if demand == "S":
    seller_function()
