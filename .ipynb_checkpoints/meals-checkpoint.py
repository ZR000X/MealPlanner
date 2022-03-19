from classes import *

U["onion"] = U.g * 250
U["tspn_garlic"] = U.g * 15
U["tspn_curry_powder"] = U.g * 3.5
U["tomato"] = U.g * 200
U["cayenne chilli"] = U.g * 8
U["tblspn olive oil"] = (U.g * 8) * (1.11 * U.ml / U.g)
U["stick of butter"] = U.g * 50
U["potato"] = U.g * 173
U["tspn_sugar"] = U.g * 6.8
U["tspn_coffee_jacobs"] = U.g * 2.3
U["tspn_coffee_nestle"] = U.g * 2.4

m = Meal(servings=4.5)
m["butter"] = U.stick*2
m["cheese sauce"] = U.g*45
m["olive oil"] = U["tblspn olive oil"] * 2
m["fusilli pasta"] = U.g*125
m["cauliflower"] = U.g*175
m["brocolli"] = U.g*175
m["salt"] = U.g * 10
m["garlic"] = U["tspn_garlic"] * 2
m["milk"] = U.cup*0.25
m["water"] = U.cup
M["Abi's Broccauli Pasta"] = m.copy()

m = Meal(servings=4)
m["pasta"] = U.g * 60
m["onion"] = U["onion"]
m["garlic"] = U["tspn_garlic"] * 2
m["green pepper"] = U.g * 250
m["mushroom"] = U.g * 250
m["tomato"] = U["tomato"] 
m["cayenne chilli"] = U["cayenne chilli"] * 2
m["olive oil"] = U["tblspn olive oil"] * 2
m["butter"] = U["stick of butter"] * 0.5
m["soya sauce"] = U["tblspn olive oil"]
m["barbeque spice"] = U.pinch
m["salt"] = U.pinch
m["herbs"] = U.pinch
m["potato"] = U["potato"] * 2
M["Abi's Stir Fry: pasta"] = m.copy()

m = Meal(servings=4)
m["butter"] = U.stick * 2
m["chicken"] = U.g * 500
m["onion"] = U["onion"]
m["garlic"] = U["tspn_garlic"]
m["Rajah curry powder"] = U["tspn_curry_powder"] * 2
m["Royco butter chicken sauce"] = U.g * 50
M["Abi's Butter Chicken"] = m.copy()

m = Meal(servings=1)
m["Indomie Noodles Hot & Spicy"] = U.g * 80
M["Indomie Noodles Hot & Spicy"] = m.copy()

m = Meal(servings=1)
m["water"] = U.cup * 0.5
m["milk"] = U.cup * 0.5
m["brown sugar"] = U["tspn_sugar"] * 2
m["jacobs coffee"] = U["tspn_coffee_jacobs"] * 2
M["Shaun's coffee"] = m.copy()

m = Meal(servings=1)
m["water"] = U.cup * 0.5
m["milk"] = U.cup * 0.5
m["brown sugar"] = U["tspn_sugar"] * 2
m["nestle coffee"] = U["tspn_coffee_nestle"] * 2
M["Abi's coffee"] = m.copy()