# Declaring a 3D array for a storage unit with different sections
storage_unit = [
    [
        ['Books', 'Notebooks'],
        ['Magazines', 'Newspapers']
    ],
    [
        ['Clothes', 'Shoes'],
        ['Hats', 'Scarves']
    ],
    [
        ['Electronics', 'Cables'],
        ['Gadgets', 'Chargers']
    ]
]

# Accessing and printing items from the storage unit
section = 1  # Second section
row = 0      # First row
column = 1   # Second column

item = storage_unit[section][row][column]
print(f"Item in Section {section}, Row {row}, Column {column}: {item}")
