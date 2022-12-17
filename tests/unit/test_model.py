from recipes_api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    recipe = Recipe('Milkshake', 'milk', 'Pour milk.')
    assert recipe.name == 'Milkshake'
    assert recipe.ingredients == 'milk'
    assert recipe.steps == 'Pour milk.'
    assert recipe.rating == 0.0
    assert recipe.favourite == False