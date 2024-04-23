from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy recipe data
recipes = [
    {"id": 1, "name": "Recipe 1", "ingredients": ["ingredient1", "ingredient2"], "image": "recipe1.jpg", "link": "recipe1link"},
    {"id": 2, "name": "Recipe 2", "ingredients": ["ingredient3", "ingredient4"], "image": "recipe2.jpg", "link": "recipe2link"},
    {"id": 3, "name": "Recipe 3", "ingredients": ["ingredient5", "ingredient6"], "image": "recipe3.jpg", "link": "recipe3link"}
]

@app.route('/recipes', methods=['POST'])
def get_recipes():
    data = request.get_json()
    ingredients = data.get('ingredients', [])
    
    # Filter recipes based on ingredients
    matched_recipes = []
    for recipe in recipes:
        if all(ingredient in recipe['ingredients'] for ingredient in ingredients):
            matched_recipes.append(recipe)
    
    return jsonify(matched_recipes)

if __name__ == '__main__':
    app.run(debug=True)
