import pytest


base_url = "https://practice-automation.com/"

@pytest.fixture(scope="function", autouse=True)
def pour_chaque_test(page):
   page.goto(base_url)
   yield


def test_form_fields(page):
   pass