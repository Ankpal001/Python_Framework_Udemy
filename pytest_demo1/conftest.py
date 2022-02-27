import pytest

@pytest.fixture()
def setup():
    print("i'll be executed first")
    yield
    print("I be executed last")