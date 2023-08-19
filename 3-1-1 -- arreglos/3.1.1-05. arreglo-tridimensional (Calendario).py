# Declaring a 3D array for a calendar with months, weeks, and days
calendar = [
    # January
    [
        # Weekdays
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        # Days
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, None, None, None, None]  # Placeholder for remaining days
    ],
    # February (considering a non-leap year)
    [
        # Weekdays
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        # Days
        [None, None, None, None, 1, 2, 3],  # Placeholder for previous days
        [4, 5, 6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15, 16, 17],
        [18, 19, 20, 21, 22, 23, 24],
        [25, 26, 27, 28, None, None, None]  # Placeholder for remaining days
    ],
    # March
    [
        # Weekdays
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        # Days
        [1, 2, 3, 4, 5, 6, 7],
        [8, 9, 10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19, 20, 21],
        [22, 23, 24, 25, 26, 27, 28],
        [29, 30, 31, None, None, None, None]  # Placeholder for remaining days
    ],
    # ... Continue with other months
]

# Accessing and printing specific day from the calendar
month = 2   # March
week = 3    # Fourth week
day = 2     # Wednesday

weekday = calendar[month][0][day]
date = calendar[month][1][day]

print(f"Date: {weekday}, {month + 1}/{date}")
