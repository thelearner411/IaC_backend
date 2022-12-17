from flask import Flask, request
from recipes_api import db, app
from recipes_api import recipe


@app.route('/')
def hello_world():
    return "Welcome to Mikhaile's Recipes! 🥘"

@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'


@app.route('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    recipe = recipe(name, ingredients, steps)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipes/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):
    recipe = recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.steps = request.json['steps']
    recipe.rating = request.json['rating']
    recipe.favourite = request.json['favourite']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'rating': recipe.rating,
        'favourite': recipe.favourite,
        'created_at': recipe.created_at
    }