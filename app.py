import os
import sqlite3
import streamlit as st

# Function to connect to the databasedefget_db_connection():
    conn = sqlite3.connect('food_and_drink.db')
    return conn

# Function to create the database and populate it if it doesn't existdefsetup_database():
    ifnot os.path.exists('food_and_drink.db'):
        conn = get_db_connection()
        c = conn.cursor()

        # Create Recipes table
        c.execute('''
        CREATE TABLE IF NOT EXISTS Recipes (
            recipe_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
        ''')

        # Create Ingredients table
        c.execute('''
        CREATE TABLE IF NOT EXISTS Ingredients (
            ingredient_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
        ''')

        # Create RecipeIngredients table
        c.execute('''
        CREATE TABLE IF NOT EXISTS RecipeIngredients (
            recipe_id INTEGER,
            ingredient_id INTEGER,
            quantity TEXT NOT NULL,
            FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id),
            FOREIGN KEY (ingredient_id) REFERENCES Ingredients (ingredient_id)
        )
        ''')

        # List of recipes (name, category)
        recipes = [
            ('Celestial Creature Gyro and Meteorite Fries', 'Grill'),
            ('Andromeda Invader Curry', 'Grill'),
            ('Crater Cinnamon Roll Pancakes', 'Grill'),
            ('Nebula Nosh Chicken & Waffles', 'Grill'),
            ('Extraterrestrial Omelet', 'Grill'),
            ('Celestial Caesar Salad', 'Grill'),
            ('Blackhole Brownies', 'Grill'),
            ('Alien Antenna Bites', 'Grill'),
            ('Orbiting Onion Rings', 'Grill'),
            ('Martian Mousse', 'Grill'),
            ('Planetary Pizza', 'Grill'),
            ('Galaxy Guac Burger and Meteorite Fries', 'Grill'),
            ('Nebula Nectar Cola', 'Cold Drinks'),
            ('Comet Cola Float', 'Cold Drinks'),
            ('Lunar Lemonade', 'Cold Drinks'),
            ('Spacecraft Smores Shake', 'Cold Drinks'),
            ('UFO Umbrella Drink', 'Cold Drinks'),
            ('Alien Ambrosia', 'Cold Drinks'),
            ('Asteroid Amaretto Sour', 'Cold Drinks'),
            ('Galactic Grape Cola', 'Cold Drinks')
        ]

        # List of ingredients (name)
        ingredients = [
            'sliced potato',
            'tzatziki',
            'pita',
            'cheese',
            'steak',
            'cinnamon',
            'flour',
            'egg',
            'sugar',
            'sightings seasoning',
            'chicken',
            'rice',
            'avocado',
            'jalapenos',
            'lettuce',
            'croutons',
            'caesar dressing',
            'cocoa powder',
            'water',
            'onion',
            'whipped cream',
            'pizza crust',
            'tomato',
            'bun',
            'cola syrup',
            'soda water',
            'milk',
            'lemon',
            'orange',
            'grape',
            'tequila',
            'vodka',
            'cracked coconut',
            'amaretto',
            'smores',
            'special ingredient'
        ]

        # List of recipe-ingredient relationships (recipe_id, ingredient_id, quantity)
        recipe_ingredients = [
            (1, 1, '1 sliced potato'),  # Celestial Creature Gyro and Meteorite Fries
            (1, 2, '1 tzatziki'),
            (1, 3, '1 pita'),
            (1, 4, '1 cheese'),
            (1, 5, '1 steak'),
            (2, 1, '1 sliced potato'),  # Andromeda Invader Curry
            (2, 10, '1 sightings seasoning'),
            (2, 11, '1 chicken'),
            (2, 12, '1 rice'),
            (3, 6, '1 cinnamon'),       # Crater Cinnamon Roll Pancakes
            (3, 7, '1 flour'),
            (3, 8, '1 egg'),
            (3, 9, '1 sugar'),
            (4, 10, '1 sightings seasoning'),  # Nebula Nosh Chicken & Waffles
            (4, 7, '1 flour'),
            (4, 11, '1 chicken'),
            (4, 8, '1 egg'),
            (5, 4, '1 sliced cheese'),  # Extraterrestrial Omelet
            (5, 13, '1 avocado'),
            (5, 8, '1 egg'),
            (5, 14, '1 jalapenos'),
            (6, 4, '1 sliced cheese'),  # Celestial Caesar Salad
            (6, 15, '1 lettuce'),
            (6, 16, '1 croutons'),
            (6, 17, '1 caesar dressing'),
            (7, 7, '1 flour'),  # Blackhole Brownies
            (7, 18, '1 cocoa powder'),
            (7, 8, '1 egg'),
            (7, 9, '1 sugar'),
            (8, 4, '1 sliced cheese'),  # Alien Antenna Bites
            (8, 7, '1 flour'),
            (8, 11, '1 chicken'),
            (8, 10, '1 sightings seasoning'),
            (9, 10, '1 sightings seasoning'),  # Orbiting Onion Rings
            (9, 7, '1 flour'),
            (9, 19, '1 sliced onion'),
            (9, 20, '1 water'),
            (10, 9, '1 sugar'),  # Martian Mousse
            (10, 18, '1 cocoa powder'),
            (10, 8, '1 egg'),
            (10, 21, '1 whipped cream'),
            (11, 23, '1 sliced tomato'),  # Planetary Pizza
            (11, 4, '1 cheese'),
            (11, 22, '1 pizza crust'),
            (11, 14, '1 jalapenos'),
            (12, 5, '1 steak'),  # Galaxy Guac Burger and Meteorite Fries
            (12, 23, '1 tomato'),
            (12, 24, '1 bun'),
            (12, 13, '1 avocado'),
            (12, 1, '1 potato'),
            (13, 25, '1 cola syrup'),  # Nebula Nectar Cola
            (13, 20, '1 ice'),
            (13, 26, '1 soda water'),
            (13, 9, '1 sugar'),
            (14, 26, '1 soda water'),  # Comet Cola Float
            (14, 21, '1 whipped cream'),
            (14, 25, '1 cola syrup'),
            (14, 27, '1 milk'),
            (15, 20, '1 water'),  # Lunar Lemonade
            (15, 28, '1 ice'),
            (15, 29, '1 sliced lemon'),
            (15, 9, '1 sugar'),
            (16, 21, '1 whipped cream'),  # Spacecraft Smores Shake
            (16, 18, '1 cocoa powder'),
            (16, 37, '1 smores'),
            (16, 27, '1 milk'),
            (16, 38, '1 special ingredient'),
            (17, 30, '1 orange'),  # UFO Umbrella Drink
            (17, 31, '1 grape'),
            (17, 32, '1 tequila'),
            (18, 33, '1 vodka'),  # Alien Ambrosia
            (18, 29, '1 sliced lemon'),
            (18, 34, '1 cracked coconut'),
            (19, 9, '1 sugar'),  # Asteroid Amaretto Sour
            (19, 35, '1 amaretto'),
            (19, 29, '1 sliced lemon'),
            (20, 31, '1 grape'),  # Galactic Grape Cola
            (20, 20, '1 ice'),
            (20, 26, '1 soda water'),
            (20, 9, '1 sugar')
        ]

        # Insert recipes into the Recipes table
        c.executemany('INSERT INTO Recipes (name, category) VALUES (?, ?)', recipes)

        # Insert ingredients into the Ingredients table
        c.executemany('INSERT INTO Ingredients (name) VALUES (?)', [(ingredient,) for ingredient in ingredients])

        # Insert the relationships between recipes and ingredients into the RecipeIngredients table
        c.executemany('INSERT INTO RecipeIngredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)', recipe_ingredients)

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        st.success('Database setup completed!')

# Run the setup only if the database doesn't exist
setup_database()

# Streamlit UI
st.title('Food & Drink Ingredient Manager')

# Search Recipe Section
st.header('Search for a Recipe')
recipe_name = st.text_input('Enter recipe name:')
if recipe_name:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        SELECT r.name, i.name, ri.quantity
        FROM Recipes r
        JOIN RecipeIngredients ri ON r.recipe_id = ri.recipe_id
        JOIN Ingredients i ON ri.ingredient_id = i.ingredient_id
        WHERE r.name LIKE ?
    ''', ('%' + recipe_name + '%',))
    results = c.fetchall()
    conn.close()

    if results:
        st.subheader(f"Ingredients for {recipe_name}:")
        for result in results:
            st.write(f"{result[1]}: {result[2]}")
    else:
        st.write("No recipe found.")

# Calculate Ingredients Section
st.header('Calculate Total Ingredients for Orders')
order_input = st.text_area('Enter orders (e.g., Andromeda Invader Curry,15):')
if order_input:
    orders = order_input.split('\n')
    total_ingredients = {}
    conn = get_db_connection()
    c = conn.cursor()

    for order in orders:
        recipe, quantity = order.split(',')
        quantity = int(quantity)
        c.execute('''
            SELECT i.name, ri.quantity
            FROM Recipes r
            JOIN RecipeIngredients ri ON r.recipe_id = ri.recipe_id
            JOIN Ingredients i ON ri.ingredient_id = i.ingredient_id
            WHERE r.name = ?
        ''', (recipe,))
        results = c.fetchall()

        for result in results:
            ingredient, qty = result[0], result[1]
            qty_value = int(qty.split()[0])  # Assumes the quantity is formatted like '1 example'if ingredient in total_ingredients:
                total_ingredients[ingredient] += quantity * qty_value
            else:
                total_ingredients[ingredient] = quantity * qty_value

    conn.close()
    st.subheader("Total Ingredients Needed:")
    for ingredient, total in total_ingredients.items():
        st.write(f"{ingredient}: {total}")
