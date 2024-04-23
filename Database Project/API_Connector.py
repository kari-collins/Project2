import mysql.connector
import requests

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="kcoll0918",
    database="What_Is_In_Your_Fridge"
)

cursor = db.cursor()

def signup():
    print("Sign Up")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    diet_pref = input("Enter your dietary preferences:\n1. Gluten Free\n2. Ketogenic\n3. Vegetarian\n4. Lacto-Vegetarian\n5. Ovo-Vegetarian\n6. Vegan\n7. Pescetarian\n8. Paleo\n9. Primal\n10. Low FODMAP\n11. Whole30\n12. None\nYour choice: ")
    cuisine_pref = input("Enter your cuisine preference:\n1. African\n2. Asian\n3. American\n4. British\n5. Cajun\n6. Caribbean\n7. Chinese\n8. Eastern European\n9. European\n10. French\n11. German\n12. Greek\n13. Indian\n14. Irish\n15. Italian\n16. Japanese\n17. Jewish\n18. Korean\n19. Latin American\n20. Mediterranean\n21. Mexican\n22. Middle Eastern\n23. Nordic\n24. Southern\n25. Spanish\n26. Thai\n27. Vietnamese\n28. None\nYour choice: ")
    ingredients = input("Enter the list of ingredients separated by comma: ")

    cuisine_id = get_cuisine_id(cuisine_pref)

    try:
        cursor.execute("INSERT INTO user (Name, Age, Email, Username, Password, DietID, CuisineID) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, age, email, username, password, diet_pref, cuisine_id))
        db.commit()
        print("User signed up successfully!")

        # Fetch recipes based on dietary preferences, cuisine, and ingredients
        fetch_recipes(diet_pref, cuisine_pref, ingredients)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()

def fetch_recipes(diet_pref, cuisine_pref, ingredients):
    # Spoonacular API parameters
    api_key = "f487a01336e74889a137b6cf3fc65c82"
    base_url = "https://api.spoonacular.com/recipes/findByIngredients"

    # Construct query parameters
    params = {
        "apiKey": api_key,
        "ingredients": ingredients,
        "number": 3,  # Number of recipes to fetch
        "diet": diet_pref,
        "cuisine": cuisine_pref
    }

    try:
        # Send GET request to Spoonacular API
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            recipes = response.json()
            print("Recipes:")
            for recipe in recipes:
                print(recipe["title"])
        else:
            print("Failed to fetch recipes. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error fetching recipes:", e)

def get_cuisine_id(choice):
    # Map user's choice to corresponding CuisineID
    cuisine_mapping = {
        "1": "African",
        "2": "Asian",
        "3": "American",
        "4": "British",
        "5": "Cajun",
        "6": "Caribbean",
        "7": "Chinese",
        "8": "Eastern European",
        "9": "European",
        "10": "French",
        "11": "German",
        "12": "Greek",
        "13": "Indian",
        "14": "Irish",
        "15": "Italian",
        "16": "Japanese",
        "17": "Jewish",
        "18": "Korean",
        "19": "Latin American",
        "20": "Mediterranean",
        "21": "Mexican",
        "22": "Middle Eastern",
        "23": "Nordic",
        "24": "Southern",
        "25": "Spanish",
        "26": "Thai",
        "27": "Vietnamese",
        "28": "None"  # Add "None" as an option
    }

    cuisine_name = cuisine_mapping.get(choice)
    if cuisine_name is None:
        return None

    # Retrieve the corresponding CuisineID from the cuisine table
    cursor.execute("SELECT CuisineID FROM cuisine WHERE CuisineName = %s", (cuisine_name,))
    result = cursor.fetchone()
    if result is None:
        print("Error: Cuisine preference not found in the database.")
        return None

    return result[0]  # Return the CuisineID

def main():
    print("1. Sign Up")
    print("2. Login")
    choice = input("Enter your choice: ")
    if choice == "1":
        signup()
    elif choice == "2":
        # Implement login functionality
        pass
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
