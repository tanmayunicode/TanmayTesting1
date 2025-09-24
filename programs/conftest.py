import pytest

@pytest.fixture()
def setup():
    print("Launch the browser window and load the url")
    yield
    print("Close the browser window")