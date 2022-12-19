from recipes_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating, favourite fields are defined correctly
    """
    recipe = Recipe('Milkshake', 'milk', 'Pour milk.', 5, True)
    assert recipe.name == 'Milkshake'
    assert recipe.ingredients == 'milk'
    assert recipe.steps == 'Pour milk.'
    assert recipe.rating == 5
    assert recipe.favourite == True