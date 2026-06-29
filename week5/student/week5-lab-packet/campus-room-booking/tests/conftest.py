import pytest

from app.storage import reset_storage


@pytest.fixture(autouse=True)
def reset_state_between_tests():
    reset_storage()
