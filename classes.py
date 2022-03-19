from copy import deepcopy

def dict_to_pairs(d):
    out = set()
    for key, value in d.items():
        out.add([key, value])
    return out

class Registry:
    def __init__(self):
        self.register = dict()
    
    def __getitem__(self, key):
        return self.register[key]
    
    def __setitem__(self, key, value):
        self.register[key] = value

class Dimension:
    def __init__(self, dims: dict):
        # check dimensions are pairs of strings and floats
        self.dims = dims
    
    def pop0s(self):
        dims = deepcopy(self.dims)
        for key, value in self.dims.items():
            if value == 0:
                dims.pop(key)
        self.dims = dims
        
    def __eq__(self, other):
        return type(other) is Dimension and self.dims == other.dims
    
    def __mul__(self, other):
        if type(other) is Dimension:
            dims = deepcopy(self.dims)
            for key, value in other.dims.items():
                if value != 0:
                    if key in dims:
                        dims[key] += value
                        if dims[key] == 0:
                            dims.pop(key)
                    else:
                        dims[key] = value
            return Dimension(dims)
        else:
            raise ValueError
    
    def __pow__(self, other):
        if type(other) is int or type(other) is float:
            dims = deepcopy(self.dims)
            for key, value in self.dims.items():
                if value != 0:
                    dims[key] = value * other
                    if dims[key] == 0:
                        dims.pop(key)
            return Dimension(dims)
        else:
            raise ValueError
    
    def __truediv__(self, other):
        if type(other) is Dimension:
            dims = deepcopy(self.dims)
            for key, value in other.dims.items():
                if value != 0:
                    if key in dims:
                        dims[key] -= value
                        if dims[key] == 0:
                            dims.pop(key)
                    else:
                        dims[key] = -value
            return Dimension(dims)
    
    def __div__(self, other):
        if type(other) is Dimension:
            dims = deepcopy(self.dims)
            for key, value in other.dims.items():
                if value != 0:
                    if key in dims:
                        dims[key] -= value
                        if dims[key] == 0:
                            dims.pop(key)
                    else:
                        dims[key] = -value
            return Dimension(dims)
        
    def __str__(self):
        out = ""
        for key, value in self.dims.items():
            if value != 0:
                out += key + ": " + str(value) +", "
        if out == "":
            return "[1]"
        return "["+out[:-2]+"]"
    
    def copy(self):
        return Dimension(deepcopy(self.dims))

class Unit:
    def __init__(self, dimension: Dimension, magnitude: float):
        self.dimension = dimension
        self.magnitude = magnitude
    
    def __add__(self, other):
        if type(other) is Unit and self.dimension == other.dimension:
            return Unit(self.dimension, self.magnitude + other.magnitude)
        raise ValueError("Trying to add unit dimensions",str(self.dimension),"and",str(other.dimension))
        
    def __sub__(self, other):
        if type(other) is Unit and self.dimension == other.dimension:
            return Unit(self.dimension, self.magnitude - other.magnitude)
        raise ValueError("Trying to add unit dimensions",str(self.dimension),"and",str(other.dimension))
    
    def __str__(self, decimals = 6):
        return str(round(self.magnitude,decimals))+" "+str(self.dimension)
    
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude * other)
        return Unit(self.dimension * other.dimension, self.magnitude * other.magnitude)
    
    def __rmul__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude * other)
        return Unit(self.dimension * other.dimension, self.magnitude * other.magnitude)
        
    def __div__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude / other)
        return Unit(self.dimension / other.dimension, self.magnitude / other.magnitude)
    
    def __rdiv__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude / other)
        return Unit(self.dimension / other.dimension, self.magnitude / other.magnitude)
    
    def __truediv__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude / other)
        return Unit(self.dimension / other.dimension, self.magnitude / other.magnitude)
        
    def __rtruediv__(self, other):
        if type(other) is int or type(other) is float:
            return Unit(self.dimension, self.magnitude / other)
        return Unit(self.dimension / other.dimension, self.magnitude / other.magnitude)
    
    def __pow__(self, other):
        return Unit(self.dimension ** other, self.magnitude ** other)
            
    def copy(self):
        return Unit(self.dimension.copy(), self.magnitude)

class UnitRegistry(Registry):
    def __init__(self):
        super().__init__()
        self.m = Unit(Dimension({"LENG": 1}), 1)
        self.km = self.m * 1000        
        self.cm = self.m * 0.01
        self.mm = self.cm * 0.1
        self.mile = self.km * 1.60934        
        
        self.kg = Unit(Dimension({"MASS": 1}), 1)
        self.g = self.kg * 0.001
        self.mg = self.g * 0.001
        self.ton = self.kg * 1000
        
        self.stick = self.g * 50
        
        self.sec = Unit(Dimension({"TIME": 1}), 1)
        self.s = self.sec
        self.min = self.sec * 60
        self.h = self.min * 60
        self.day = self.h * 24
        self.year = self.day * 365.25
        
        self.l = Unit(Dimension({"LITR": 1}), 1)
        self.ml = self.l * 0.001
        self.kl = self.l * 1000
        self.cup = self.ml * 250
        
        self.pinch = self.g * 0.355625
        
        self.serving = Unit(Dimension({"SERV": 1}), 1)
        
        self.R = Unit(Dimension({"MONE": 1}), 1)
        
        self.mps = self.m / self.sec
        self.N = self.kg * self.m / self.sec ** 2 # Newton, unit of force
                      
        self.MASS = self.kg
        self.LENGTH = self.m
        self.TIME = self.sec
        self.LITRE = self.l
        self.MONEY = self.R
        self.VELOCITY = self.LENGTH / self.TIME

U = UnitRegistry()

class Product:
    """
    Class for recording the actual purchaseable items on the shelf
    
    @param cost: the MONE amount to purchase
    @param quantity: the total amount that you can purchase
    @param subunit: e.g., if you buy 6 pies, then each pie is a subunit
    @param tags: a set of strings that are identifiable with the product
    """
    def __init__(self, cost: float, quantity: Unit, subunit = None, tags: set = None):
        self.cost = cost if type(cost) is Unit else U.R * cost
        self.quantity = quantity
        self.subunit = subunit
        self.tags = tags
    
    def cpuq(self):
        return self.cost / self.quantity
    
    def __lt__(self, other):
        return type(other) is Product and self.cpuq().magnitude < other.cpuq().magnitude
    
class ProductRegistry(Registry):
    def lookup(self, name):
        out = None
        for product in self.register.values():
            if name in product.tags and (out is None or out > product):
                out = product
        return out
    
    def price(self, name):
        look = self.lookup(name)
        if look is not None:
            return look.cpuq()
        return None
    
    def pricestr(self, name):
        return str(self.price(name))

PR = ProductRegistry()

class PriceRegistry(Registry):
    pass

P = PriceRegistry()

class Meal:
    def __init__(self, servings: float, ingredients: dict = None):
        if ingredients is None:
            ingredients = dict()
        self.ingredients: dict = ingredients
        self.servings = servings if type(servings) is Unit else U.serving * servings
        
    def iq(self):
        out = dict()
        for s in self.substances:
            out[s] = str(self.substances[s])
        return out
    
    def cost(self, prices, return_missing= False):
        cost = U.R * 0
        missing = set()
        if type(prices) is PriceRegistry:
            for name, portion in self.ingredients.items():
                try: 
                    cost += portion * prices[name]
                except KeyError: 
                    missing.add(name)
                except ValueError as e:
                        print(e,"item name",name)
        if type(prices) is ProductRegistry:
            for name, portion in self.ingredients.items():
                # print(cost)
                item_cost = prices.price(name)
                if not type(item_cost) is Unit:
                    missing.add(name)
                else:
                    try:
                        cost += item_cost * portion
                    except ValueError as e:
                        print(e,"item name",name)
        if return_missing:
            return [cost / self.servings, missing]
        return cost / self.servings
    
    def copy(self):
        return Meal(ingredients = deepcopy(self.ingredients), servings= self.servings)
    
    def detail(self, prices, name=""):
        cost = self.cost(prices, True)
        out = name + " MEAL COST PER SERVING: "+str(cost[0].magnitude)+"\n"
        out += "-------------------------\n"
        out += "MISSING PRICES: \n"
        for m in cost[1]:
            out += m+"\n"
        out += "-------------------------\n"
        return out

    def __getitem__(self, key):
        return self.ingredients[key]
    
    def __setitem__(self, key, value):
        self.ingredients[key] = value
        
class MealRegistry(Registry):    
    def print_meals(self):
        for name in M.register:
            print(name)
            
    def print_detail(self, name, prices):
        print(self[name].detail(prices))

M = MealRegistry()

class DayMenu:
    def __init__(self, meals: list, slots: int = 3):
        if len(meals) < slots:
            raise ValueError("Not enough meals for slots")
        self.meals = meals[:slots]
        
    def cost(self, prices):
        cost = 0 * U.MONEY
        for meal in self.meals:
            cost += meal.cost(prices) * U.serving
        return cost