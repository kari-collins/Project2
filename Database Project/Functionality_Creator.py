import mysql.connector

def get_recipes_by_cuisine(cuisine):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kcoll0918",
        database="What_Is_In_Your_Fridge"
    )
    
    # Create a cursor object to execute SQL queries
    cursor = db_connection.cursor()

    # Execute SQL query to retrieve recipes of the specified cuisine type
    sql_query = "SELECT * FROM Recipes WHERE cuisine_type = %s"
    cursor.execute(sql_query, (cuisine,))
    
    # Fetch all rows from the result set
    recipes = cursor.fetchall()
    
    # Close cursor and database connection
    cursor.close()
    db_connection.close()
    
    return recipes

# Example usage: Retrieve recipes of Italian cuisine
italian_recipes = get_recipes_by_cuisine('Italian')
for recipe in italian_recipes:
    print(recipe)  # You can format the output as needed
