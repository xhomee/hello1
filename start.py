from game_data import MENU, resources
# TODO create first


#print(MENU["latte"]["ingredients"]["water"])


def report():
    #print(resources)
    water = resources["water"]
    coffee = resources["coffee"]
    milk = resources["milk"]
    return water, coffee, milk

water, coffee, milk = report()
print(report())



def coins(how):
    quarters = int(input("how many quarters?"))
    return quarters * how


def show_element(element):
    """return list elements coffee"""
    element_list = []
    ingredients = MENU[element]["ingredients"]
    for key in ingredients:
        #element_list.append(key)
        element_list.append(ingredients[key])
    element_list.append(MENU[element]["cost"])
    #print(element_list)
    return element_list


def check_resources(report, element_list):
    new_water = water-element_list[0]
    new_coffee = coffee-element_list[1]

    print(new_water)
    print(new_coffee)
    #report[0] -= element_list[0]

    #print(len(element_list))
    print(element_list) #['water', 250, 'coffee', 24, 'milk', 100, 2.5] [250, 24, 100, 3.0]
    print(report)#(300, 200, 100) (300, 100, 200)
    print("dsfg")



# print(show_element('espresso'))
# print(" ")
# print(show_element('latte'))

ask_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
#print(show_element(ask_user))

check_resources(report(), show_element(ask_user))
# for key in MENU:
#     print(key)
#     print(MENU[key]['ingredients']['water'])

#
# ask_user = input("What would you like? (espresso/latte/cappuccino): ").lower()
#
# #show_element(ask_user)
# key, ingredients_key, cost = show_element(ask_user)
# print(key, ingredients_key, cost)
# report()





# "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }