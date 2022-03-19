from classes import *

# Example custom units
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

# Example meal creation
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
M["Broccauli Pasta"] = m.copy()