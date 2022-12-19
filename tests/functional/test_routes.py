from recipes_api import app
import pytest

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipe' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/recipes', json={'name': 'Milkshake', 'ingredients': 'milk', 'steps': 'Pour milk.', 'rating': 4, 'favourite': True})
    assert response.status_code == 200

def test_get_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/recipes/1')
    assert response.status_code == 200

def test_update_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.put('/recipes/1', json={'name': 'Boiled Egg', 'ingredients': 'egg, water', 'steps': 'Place pan of water over medium heat for 5 minutes. Add egg and leave for 8 minutes before removing from fire.', 'rating': 3.0, 'favourite': True})
    assert response.status_code == 200

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipe' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200

def test_base_path_post(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.post('/', json={'name': 'Boiled Egg', 'ingredients': 'egg, water', 'steps': 'Place pan of water over medium heat for 5 minutes. Add egg and leave for 8 minutes before removing from fire.', 'rating': 2, 'favourite': False})
    assert response.status_code == 405


