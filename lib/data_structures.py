spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_names = [food["name"] for food in spicy_foods]
    return spicy_foods_names
    

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]
    

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}' )

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    result = [food for food in spicy_foods if food["cuisine"] == cuisine]
    
    if result:
        food = result[0]
        return {
            'cuisine': food['cuisine'],
            'name': food['name'],
            'heat_level': food['heat_level']
        }
    return None 
            

def print_spiciest_foods(spicy_foods):
    result = [food for food in spicy_foods if food["heat_level"] > 5]
    
    if result:
        for food in result:
            heat = "🌶" * food["heat_level"]
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')
    else:
        print("No foods with a heat level greater than 5.")
    
    

def get_average_heat_level(spicy_foods):
   total_heat = sum(food["heat_level"] for food in spicy_foods)
   length = len(spicy_foods)
   return total_heat/length

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    
    

get_names(spicy_foods)
get_spiciest_foods(spicy_foods)
print_spicy_foods(spicy_foods)
get_spicy_food_by_cuisine(spicy_foods, "American")
print_spiciest_foods(spicy_foods)
get_average_heat_level(spicy_foods)
create_spicy_food(spicy_foods,{ "name": "Griot","cuisine": "Haitian","heat_level": 10})