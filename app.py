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

        # Example data insertion (replace this with your actual data)
        recipes = [
            ('Celestial Creature Gyro and Meteorite Fries', 'Grill'),
            ('Andromeda Invader Curry', 'Grill'),
            # Add more recipes here
        ]

        ingredients = [
            ('sliced potato'),
            ('tzatziki'),
            ('pita'),
            ('cheese'),
            ('steak'),
            # Add more ingredients here
        ]

        recipe_ingredients = [
            (1, 1, '1 sliced potato'),  # Celestial Creature Gyro and Meteorite Fries uses 1 sliced potato
            (1, 2, '1 tzatziki'),       # Celestial Creature Gyro and Meteorite Fries uses 1 tzatziki
            (1, 3, '1 pita'),           # Celestial Creature Gyro and Meteorite Fries uses 1 pita
            (1, 4, '1 cheese'),         # Celestial Creature Gyro and Meteorite Fries uses 1 cheese
            (1, 5, '1 steak'),          # Celestial Creature Gyro and Meteorite Fries uses 1 steak# Add more recipe ingredients here
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

# Your existing Streamlit app code goes here...# Streamlit UI
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
    conn = get_db_connection()
    c = conn.cursor()
    total_ingredients = {}

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
            qty_value = int(qty.split()[0])
            if ingredient in total_ingredients:
                total_ingredients[ingredient] += quantity * qty_value
            else:
                total_ingredients[ingredient] = quantity * qty_value

    conn.close()
    st.subheader("Total Ingredients Needed:")
    for ingredient, total in total_ingredients.items():
        st.write(f"{ingredient}: {total}")
