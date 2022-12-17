import pytest
from recipes_api.models import Recipe
from recipes_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    account = Recipe('Sandwich Recipe', 'bread, cheese', '1. Place cheese between bread slices')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()