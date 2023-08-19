# Declaring a 2D array for a weekly shopping list
weekly_shopping = [
    ['Monday', 'Apples', 'Bananas', 'Milk'],
    ['Tuesday', 'Bread', 'Eggs', 'Cheese'],
    ['Wednesday', 'Chicken', 'Rice', 'Vegetables'],
    ['Thursday', 'Yogurt', 'Granola', 'Berries'],
    ['Friday', 'Pasta', 'Tomato Sauce', 'Salad'],
    ['Saturday', 'Steak', 'Potatoes', 'Broccoli'],
    ['Sunday', 'Ice Cream', 'Snacks', 'Soda']
]

# Accessing and printing the shopping list for a specific day
day_index = 3  # Thursday
day = weekly_shopping[day_index][0]
items = weekly_shopping[day_index][1:]
print(f"Shopping List for {day}: {', '.join(items)}")
