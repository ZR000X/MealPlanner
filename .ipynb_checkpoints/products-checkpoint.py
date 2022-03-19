from classes import *

i = "Checkers potato"
U[i] = U.g * 173 
PR[i] = Product(cost=30, quantity=U.kg*2, subunit=U[i], tags=set([i, "potato"]))


i = "Another potato"
U[i] = U.g * 173 
PR[i] = Product(cost=29, quantity=U.kg*2, subunit=U[i], tags=set([i, "potato"]))


i = "broccauli"
PR[i] = Product(cost=25, quantity=U.g*350, tags=set([i]))
i = "carrot"
PR[i] = Product(cost=13, quantity=U.kg*1, tags=set([i]))
i = "banana"
PR[i] = Product(cost=35, quantity=U.kg*1.2, tags=set([i]))
i = "mixed peppers"
U[i] = U.g * 150
PR[i] = Product(cost=37, quantity=U.kg*1, subunit=U[i]*4, tags=set([i]))
i = "Crystal Valley salted butter"
PR[i] = Product(cost=130, quantity=U.kg*2, tags=set([i, "salted butter", "butter"]))
i = "Readymade Greek pasta salad"
PR[i] = Product(cost=65, quantity=U.g*500, tags=set([i, "greek pasta salad"]))
i = "Sasko wholewheat brown bread"
U["brown bread slice"] = U.g * (800 / 16)
PR[i] = Product(cost=20, quantity=U.g*800, subunit=U["brown bread slice"], tags=set([i, "brown bread"]))
i = "Rich and Creamy ice cream"
PR[i] = Product(cost=55, quantity=U.l*1.8, tags=set([i, "ice cream"]))
i = "Checkers mixed veg"
PR[i] = Product(cost=23, quantity=U.kg*1, tags=set([i, "mixed veg"]))
i = "Ouma's choc chip rusks"
PR[i] = Product(cost=45, quantity=U.g*450, tags=set([i, "rusks"]))
i = "Checkers full cream uht milk"
PR[i] = Product(cost=70, quantity=U.l*6, tags=set([i, "milk"]))
i = "Future life value pack"
PR[i] = Product(cost=100, quantity=U.kg*1.25, tags=set([i, "future life", "FL"]))
i = "Royco butter chicken sauce"
PR[i] = Product(cost=19, quantity=U.g*50, tags=set([i, "butter chicken sauce"]))